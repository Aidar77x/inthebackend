class Reservation(models.Model):
    STATUS_CHOICES = [
        ("waiting", "Ожидание"),
        ("confirmed", "Подтверждено"),
        ("canceled", "Отменено"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="waiting")

    def __str__(self):
        return f"Reservation {self.id} for {self.user.username}"
