#julia

module types 

type Body{T}
    mass::T
    velocity::Vector{T}
    radius::T
    position::Vector{T}
end

#Creates a new type Moon with atttributes of Body but is treated as separate type
typealias Moon Body

type Command_Module{T}
    mass::T
    velocity::Vector{T}
    radius::T
    position::Vector{T}
    positionE::Vector{T}
    positionH::Vector{T}
    velocityE::Vector{T}
    velocityH::Vector{T}
end

#non parametric types dont take any arguments
type EarthMoonSystem
    time::Float64
    earth::Body
    moon::Moon
    command_module::Command_Module
end

end
