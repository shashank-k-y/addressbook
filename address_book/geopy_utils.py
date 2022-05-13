from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="address_book")


def get_location_co_ordinates(address: str) -> object:
    location = geolocator.geocode(address)
    if not location:
        return None

    return (location.latitude, location.longitude)


def get_address_details_from_coordinates(co_ordinates: tuple) -> object:
    return geolocator.reverse(co_ordinates[0], co_ordinates[1])
