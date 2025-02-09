from rest_framework.serializers import ModelSerializer
from wishlists.models import Wishlist
from rooms.serializer import RoomListSerializer


class WishlistSerializer(ModelSerializer):

    rooms = RoomListSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Wishlist
        fields = (
            "name",
            "rooms",
        )
