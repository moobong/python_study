# 파이썬 클래스


## 1. 클래스 기본

### 클래스 정의:

```python
class ClassName:
    # 클래스 내용
```

### 클래스의 예:

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says Woof!")
```

### 객체 생성:

```python
my_dog = Dog("Buddy")
```

### 메서드 호출:

```python
my_dog.bark()  # 출력: Buddy says Woof!
```

## 2. 생성자 `__init__`:

위의 `Dog` 클래스에 있는 `__init__` 메서드는 생성자라고 합니다. 객체가 생성될 때 자동으로 호출됩니다.

## 3. 인스턴스 변수:

`self.name`은 인스턴스 변수입니다. `self`는 현재 객체의 인스턴스를 참조하며, 각 객체는 고유한 인스턴스 변수를 가집니다.

## 4. 메서드:

`bark`는 클래스 `Dog`의 메서드입니다. 메서드는 클래스 내의 함수로, 특정 데이터(인스턴스 변수)와 관련된 동작을 정의합니다.

## 5. 클래스 변수:

모든 객체에 공통적인 값을 저장할 수 있는 변수입니다.

```python
class Dog:
    species = "Canine"  # 클래스 변수

    def __init__(self, name):
        self.name = name
```

## 6. 상속:

한 클래스가 다른 클래스의 기능을 상속받을 수 있습니다. 

```python
class GoldenRetriever(Dog):
    def fetch(self, item):
        print(f"{self.name} fetched the {item}!")
```


## 7. 고급 기능

### 1. 정적 메서드 (`@staticmethod`):

정적 메서드는 클래스의 인스턴스 없이 호출할 수 있으며, `self` 인자를 사용하지 않습니다. 

```python
class MyClass:
    @staticmethod
    def static_method():
        print("This is a static method.")
```

### 2. 클래스 메서드 (`@classmethod`):

클래스 메서드는 클래스의 인스턴스 없이 호출할 수 있습니다. 첫 번째 인자로 클래스 자체를 받습니다.

```python
class MyClass:
    @classmethod
    def class_method(cls):
        print("This is a class method.")
```

### 3. 속성 (Properties):

`@property` 데코레이터를 사용하여 속성을 정의하고, 속성 값을 가져오거나 설정할 때 추가적인 로직을 수행할 수 있습니다.

```python
class MyClass:
    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        print("Getting x")
        return self._x

    @x.setter
    def x(self, value):
        print("Setting x")
        self._x = value
```

### 4. 매직 메서드 (Magic methods):

두 객체를 더하거나, 문자열로 표현하거나, 비교하는 등의 동작을 정의할 때 사용합니다. 예를 들면:

```python
class MyClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"MyClass({self.value})"
    
    def __add__(self, other):
        return MyClass(self.value + other.value)
```

### 5. 비공개 속성과 메서드 (Private attributes and methods):

언더스코어 (`_`)를 변수나 메서드 이름 앞에 붙여 비공개로 만들 수 있습니다. 

```python
class MyClass:
    def __init__(self):
        self.public_var = "I'm public!"
        self._private_var = "I'm semi-private!"

    def public_method(self):
        return "This is a public method."

    def _private_method(self):
        return "This is a private method."
```

### 6. 클래스의 컴포지션:

한 클래스가 다른 클래스의 객체를 포함하는 방식입니다. 상속과 비교하여, 때로는 컴포지션이 더 적합한 방식일 수 있습니다.

```python
class Engine:
    pass

class Car:
    def __init__(self):
        self.engine = Engine()
```



