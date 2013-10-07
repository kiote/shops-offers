require 'sinatra/base'
require 'sinatra/config_file'
require 'json'

class Offers < Sinatra::Base
  register Sinatra::ConfigFile
  config_file 'config.yml'

  get '/' do
    "Hell"
  end

  # start the server if ruby file executed directly
  run! if app_file == $0
end
