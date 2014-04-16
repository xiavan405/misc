using constants
using types
include("physics.jl")
include("moon.jl")
include("command-module.jl")
include("system.jl")
 
# initialization of our bodies
earth = Body(ME, [0.0, 0.0], RE, ORIGIN)
moon = Moon(MM, [0., 0.], RM, moon_position(0.0))
command_module = Command_Module(MCM, INITIAL_VELOCITY, 5.0, INITIAL_POSITION, INITIAL_POSITION, INITIAL_POSITION, INITIAL_VELOCITY, INITIAL_VELOCITY)
world = System(0.0, earth, moon, command_module)
 
function simulate()
    boost = 10
    position_list = Vector{Float64}[]
    current_time = 1.
    h = 0.1 # s, set as initial step size right now but will store current step size
    h_new = h # s, will store the adaptive step size of the next step
 
 
    while current_time <= TOTAL_DURATION
        update(world, current_time, h)
 
        positionE = world.command_module.positionE
        positionH = world.command_module.positionH
        velocityE = world.command_module.velocityE
        velocityH = world.command_module.velocityH
 
        error_amt = norm(positionE - positionH) + TOTAL_DURATION * norm(velocityE - velocityH)
        h_new = min(0.5 * MARKER_TIME, max(0.1, h * sqrt(TOLERANCE / error_amt))) # Restrict step size to reasonable range
 
        current_time += h
        h = h_new
 
        push(position_list, copy(world.command_module.position))
    end
 
    return position_list
end
 
@time pos = simulate()
writecsv("output.csv", pos)
