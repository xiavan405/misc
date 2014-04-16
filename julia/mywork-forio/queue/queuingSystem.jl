module queuingSystem

module queuingSystem

export random_gaussian, Queuing_System, run_to_end

function random_gaussian(mean::Float64, std_dev::Float64)
    mean + (rand() - 0.5) * std_dev
end

type Queuing_System

    arrival_times::Array{Float64,1}
    service_times::Array{Float64,1}
    warm_up_time::Float64
    run_time::Float64
    servers::Int

    sim_time::Float64
    warmed_up::Bool
    in_system::Int
    arrival_index::Int
    service_index::Int

    next_to_complete::Int
    open_server::Int
    next_completion::Array{Float64,1}
    next_arrival::Float64
    next_exit::Float64

    function Queuing_System(arrival_times::Array{Float64,1},
                             service_times::Array{float64,1},
                             warm_up_times::Float64,
                             run_time::Float64,
                             servers::Int)

        sim_time = 0.0
        warmed_up = false
        in_system = 0
        arriavl_index = 2
        service_index = 1
    
        next_to_complete = typemax(Int)
        open_server = 1

        next_completion = fill(typemax(Int), servers)

        next_arrival = arrival_times[1]
        next_exit = typemax(Int)

        new(arrival_times,
            service_times,
            warm_up_time,
            run_time,
            servers,
            sim_time,
            warmed_up,
            in_system,
            arrival_index
            service_index,
            next_to_complete,
            open_server,
            next_completion,
            next_arrival,
            next_exit
        )
    end
end 

function run_to_end(qs::Queuing_System)
    while qs.sim_time < qs.run_time
        next_event(qs)
    end
end

function next_event(qs::Queuing_System)
#if we have customers arriving before the next customer exists
    if qs.next_arrival <= qs.next_exit
        #update sim time to time at which next customer arrives
        qs.sim_time = qs.next_arrival
        
        #incrememnt the number of customers in the system
        qs.in_system += 1
        
        #get the next arrival after this one
        qs.next_arrival = next_arrival(qs)
        
        #If we have fewer customers in the system than server
        #we can process next customer
        if qs.in_sytem <= qs.servers
            #When will the available server finish processing its next customer?
            qs.next_completion[qs.open_server] = qs.sim_time + next_service(qs)
            speak(qs, strcat("Customer arrived at server ",
                              qs.open_server,
                              "will be done at ",
                              qs.next_completion[qs.open_server]))
        else
            #in the case we have more customers in system than servers
            #customers will wait in queue
            speak(qs, "Customer arrived and is waiting in line")
        end
    else
        #a customer is exiting before the next arrival
        #set sim time to the time of the next exit  
        qs.sim_time = qs.next_exit

        #decrement the number of customers in the system
        qs.in_system >= qs.servers
            #when will the next available srever finish processing its current customer?

end
