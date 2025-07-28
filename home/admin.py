from django.contrib import admin
from django.http import HttpResponse
from .models import Subscription
from reportlab.pdfgen import canvas

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at')
    actions = ['export_to_pdf']

    def export_to_pdf(self, request, queryset):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="subscriptions.pdf"'

        p = canvas.Canvas(response)
        p.setFont("Helvetica", 12)

        y = 800  # posisi awal tulisan
        p.drawString(200, 820, "Daftar Email Subscriptions")
        p.setFont("Helvetica", 10)

        for sub in queryset:
            p.drawString(100, y, f"- {sub.email}")
            y -= 20
            if y < 50:  # halaman baru jika penuh
                p.showPage()
                p.setFont("Helvetica", 10)
                y = 800

        p.save()
        return response

    export_to_pdf.short_description = "Ekspor email terpilih ke PDF"
