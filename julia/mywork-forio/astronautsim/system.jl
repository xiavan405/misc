#julia 

function update(me::System, time::Float64)
    #'me' is a reference to this instance of system

    me.time = time 
    #Explicitly set the time on the system
    
    #using julias multiple dispatch to separate methods for different arg types/combinations
    update(me.moon, time) #update moon
    update(me.command_module, time) #update command_module

    return me
end
