require 'compass'
require 'compass/exec'

def compile_sass()
  compass = Compass::Exec::SubCommandUI.new(['watch', '_compass'])
  t = Thread.new { compass.run! }
end

if Jekyll.configuration({})['foundation-dev-mode']
  compile_sass()
end

