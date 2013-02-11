# Copyright (c) by it's authors. 
# Some rights reserved. See LICENSE, AUTHORS.

from abstractQuery import AbstractQuery
from peer import Peer
from viewer import Viewer
from valueQueryResult import ValueQueryResult

class DocumentListQuery(Viewer, AbstractQuery):
    def __init__(self, room):
        Viewer.__init__(self, room, self._changed, "_id")
        AbstractQuery.__init__(self)

        self._viewer = None
        self._lastQuery = None

    def _changed(self, _id):
        if _id is not None and self._lastQuery is not None:
            self._query(None, self._lastQuery)
            self._lastQuery = None

    def _query(self, pillow, query):
        if query is None: return
        if self._document is None: 
            self._lastQuery = query
            return

        path = query.get('args.path')
        filters = query.get('args.filter')

        if path is None: return

        import re
            
        values = []
        _values = self.document().get(path)

        if isinstance(_values, list): values = _values
        elif isinstance(_values, dict):
            for key in sorted(_values.keys()):
                value = _values[key]
                if isinstance(value, dict):
                    import copy
                    value = copy.deepcopy(value)
                    value["id"] = value["__key__"] = key
                else:
                    value = {"id": key, "__value__": value, "__key__": key}

                ok = True
                if filters != None:
                    for filter in filters:
                        for path, f in filter.items():
                            v = None
                            if path in value: v = value[path]
                                
                            if f.startswith('!'):
                                f = f[1:]
                                if v is None or not re.match(f, v): continue
                            else:
                                if f in ("*", ".*") or (v is not None and re.match(f, v)): continue

                            ok = False
                            break
               
                if ok: values.append(value) 

        self._throw(AbstractQuery.Out.Result, ValueQueryResult(self, query, values, self._roomName))
