#julia

module constants

export ME, RE, G, MM, RM, MCM, DISTANCE_TO_MOON, MOON_PERIOD, MOON_INITIAL_ANGLE, ORIGIN
export TOTAL_DURATION, MARKER_TIME, TOLERANCE, INITIAL_POSITION, INITIAL_VELOCITY

#mass eart kg
const ME = 5.97e24
#radius earth
const RE = 6.378e6
#gravity const
const G = 6.67e-11
#mass moon kg
const MM = 7.35e22
#radius moon 
const RM = 1.74e6
#mass command module kg
const MCM = 5000.
const DISTANCE_TO_MOON = 400.5e6
const MOON_PERIOD = 27.3 * 24.0 * 3600.
const MOON_INITIAL_ANGLE = pi / 180. * -61.
const ORIGIN = [ 0., 0 ]

const TOTAL_DURATION = 12. * 24. * 3600.
const MARKER_TIME  = 0.5 * 3600.
const TOLERANCE = 100000.

#vector,velocity for spacecraft 
const INITIAL_POSITION = [-6.701e6, 0.]
const INITIAL_VELOCITY = [0, -10.818e3]

end
