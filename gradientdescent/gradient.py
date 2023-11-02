import numpy as np
def gradient_descent(x, y):
    m_curr = b_curr = 0
    iterations = 10000
    learning_rate=0.01
    n=len(x)
    for i in range(iterations):
        y_predicted = m_curr * x + b_curr
        dm=-(2/n)*sum(x*(y-y_predicted))
        db = -(2 / n) * sum(y - y_predicted)
        m_curr=m_curr-learning_rate*dm
        b_curr=b_curr-learning_rate*db
        print("m {},b {},iteration {}".format(m_curr,b_curr,i))
x=np.array([1,2,3,4,5])
y=np.array([5,7,9,11,13])
gradient_descent(x,y)