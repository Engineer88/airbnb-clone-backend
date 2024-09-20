from django.db import models
from common.models import CommonModel


class Booking(CommonModel):
    """Booking Model Definition"""

    class BookingKincChoices(models.TextChoices):
        ROOM = "room", "Room"
        EXPERIENCE = "experience", "Experience"

    kind = models.CharField(
        max_length=250,
        choices=BookingKincChoices.choices,
    )

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )

    room = models.ForeignKey(
        "rooms.Room",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    experience = models.ForeignKey(
        "experiences.Experiences",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    check_in = models.DateField(
        null=True,
        blank=True,
    )
    check_out = models.DateField(
        null=True,
        blank=True,
    )

    experience_Time = models.DateTimeField(
        null=True,
        blank=True,
    )

    guests = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.kind.title()} booking for: / {self.user}"
