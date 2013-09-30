from org.bukkit.event import Listener


class NonExistentPriorityException(Exception):
    pass

class BaseListener(Listener):

    __priorities = ["highest","high","normal","low","lowest","monitor"]

    def onEnable(self):
        pass

    def onDisable(self):
        pass

    def register_event(self, func, event_class, priority='normal'):
        if priority.lower() not in __priorities:
            raise NonExistentPriorityException()

        if not hasattr(self, '_event_handlers'):
            self._event_handlers = list()

        self._event_handlers.append(dict(method=func, event=event_class, priority=priority.lower()))