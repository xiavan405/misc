#julia

function derivative(f)
    return function(x)
        #small h value
        h = x == 0
        #floating pt arithmetic gymnastics
        xph = x +h
    
        dx = xph - x
        #evaluate f at x + h
        f1 = f(xph)
        #evaluate f at x 
        f0 = f(x)
        #divid the difference by h
        return (f1 - f0) / dx
    end
end
