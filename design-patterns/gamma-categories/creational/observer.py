"""
Observer Pattern - An observer is an object that wishes to be informed about events happening in the system. The entity generating the events is an observable.

-   We need to be informed when certain things happen
    ├── Object's property changes
    ├── Object does something
    ├── Some external event occurs

-   We want to listen to events and be notified when they occurs
    ├── Notifications should include useful data

-   We want to unsubscribe from events if we are no longer interested
"""
from abc import ABC, abstractmethod
from random import randrange


class Subject(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers
    """

    @abstractmethod
    def attach(self, observer) -> None:
        """
        Attaches an observer to the subject
        """
        pass

    @abstractmethod
    def detach(self, observer) -> None:
        """
        Detach an observer from the subject
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all observers about an event
        """
        pass


class ConcreteSubject(Subject):
    """
    The Subject owns some important state and notifies observers when the state changes.
    """
    _state: int = None
    """
    For the sake of simplicity, the Subject's state. essential to all subscribers, is stored in this variable.
    """
    _observers = []

    def attach(self, observer) -> None:
        print("Subject: Attached an observer")
        self._observers.append(observer)

    def detach(self, observer) -> None:
        self._observers.remove(observer)

    """
    The subscription management methods
    """

    def notify(self) -> None:
        """
        Trigger an update in each subscriber
        """
        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        """
        Usually, the subscription logic is only a fraction of what a Subject can really do. Subjects commonly hold some important business logic, that triggers a notification method whenever something important is about to happen (or after it). 
        """
        print("\nSubject: I'm doing something important.")
        self._state = randrange(0, 10)

        print(f"\nSubject: My state has just changed to: {self._state}")
        self.notify()


class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Receive update from subject
        """
        pass


class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state < 3:
            print("Concrete Observer A: Reacted to the event")

class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 0 or subject._state >= 2:
            print("ConcreteObserverB: Reacted to the event")

if __name__ == '__main__':
    subject = ConcreteSubject()

    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    subject.some_business_logic()
    subject.some_business_logic()

    subject.detach(observer_a)

    subject.some_business_logic()
