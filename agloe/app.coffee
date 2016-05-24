# Agloe

App =
  init: ->
    console.log "init success"

  initMap: ->
    map = new google.maps.Map(
      document.getElementById('map'),
        center:
          lat: -34.397
          lng: 150.644
        zoom: 8
    )

module.exports = App
