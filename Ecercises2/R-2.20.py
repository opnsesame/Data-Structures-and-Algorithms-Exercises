'''
What are some potential efficiency disadvantages of having very 
deep inheritance trees, that is, a large set of classes, A, B, C,
and so on, such that B extends A, C extends B, D extends C, etc.?
'''
'''
Everytime you invoke a subclass from a superclass you are doing a method call so if you have nested five classes and invoke a method in the base class you will be doing five method invocations. Most compilers/runtimes will try to recognose this and optimise the extra calls away but it is only safe to do this for very simple cases.

super may be called many times over in a deep inheritance tree when calling the constructor for the deepest class. Also, if there is a method signature that is overridden in each class, the compiler will take longer to sort out or determine which method is overridden.

a bunch of classes extending one class becomes disorganized.
'''
