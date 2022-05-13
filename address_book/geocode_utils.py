from geopy.geocoders import Nominatim

import haversine as hs

geolocator = Nominatim(user_agent="address_book")


def get_location_co_ordinates(address: str) -> object:
    location = geolocator.geocode(address)
    if not location:
        return None

    return (location.latitude, location.longitude)


def get_address_details_from_coordinates(co_ordinates: tuple) -> object:
    return geolocator.reverse(co_ordinates[0], co_ordinates[1])


def find_distance_between_locations(
    user_location_co_ordinates: tuple, address_location_co_ordinates: tuple
) -> float:
    return hs.haversine(
        user_location_co_ordinates, address_location_co_ordinates
    )


def get_addresses_within_given_distance(
    user_location_co_ordinates: tuple, distance: float, addresses_list: list
) -> list:
    address_within_distance_list = []
    for address in addresses_list:
        address_co_ordinates = (address.latitude, address.longitude)

        distance_between_locations = find_distance_between_locations(
            user_location_co_ordinates=user_location_co_ordinates,
            address_location_co_ordinates=address_co_ordinates
        )

        if distance_between_locations <= distance:
            address.distance = ("%.2f" % distance_between_locations) + ' km'
            address_within_distance_list.append(address)

    return address_within_distance_list
