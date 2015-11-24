import stampery

stampery = Stampery('830fa1bf-bee7-4412-c1d3-31dddba2213d')

print stampery.get("8d35d6a20140ac7dac9fdb9f51627899b20749ea87609f3a5d337dab5dff7c70")

print stampery.stamp({'bla': 'bla'})

print stampery.stamp({'blas': 'hhh'}, open('/Users/user/Desktop/Artboard 2.png', 'rb'))
