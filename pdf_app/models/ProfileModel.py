from django.db import models
from utils.model import Model
from django_extensions.db.models import ActivatorModel, TimeStampedModel

from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from PyPDF2 import PdfFileWriter, PdfFileReader


class Profile(ActivatorModel, TimeStampedModel, Model):
    name = models.CharField(
        db_column='name',
        max_length=200
    )
    email = models.EmailField(
        db_column='email',
    )
    phone = models.CharField(
        db_column='phone',
        max_length=200
    )
    summary = models.CharField(
        db_column='summary',
        max_length=200
    )
    degree = models.CharField(
        db_column='degree',
        max_length=200
    )
    school = models.CharField(
        db_column='school',
        max_length=200
    )
    university = models.CharField(
        db_column='university',
        max_length=200
    )
    previousWork = models.TextField(
        db_column='previous_work',
        max_length=1000
    )
    skills = models.TextField(
        db_column='skills',
        max_length=1000
    )
    pdf = models.FileField(
        db_column='pdf',
        upload_to='media/pdf/',
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs):
        buffer = BytesIO()
        p = canvas.Canvas(buffer, pagesize=A4)

        # DOCUMENT DATA
        data = {
            'Name': f'{self.name}',
            'Email': f'{self.email}',
            'Phone': f'{self.phone}',
            'Summary': f'{self.summary}',
            'Degree': f'{self.degree}',
            'School': f'{self.school}',
            'University': f'{self.university}',
            'PreviousWord': f'{self.previousWork}',
            'Skills': f'{self.skills}'
        }

        # DOCUMENT CUSTOMIZATION
        p.setFont('Helvetica', 15, leading=None)
        p.setFillColorRGB(0.29296875, 0.453125, 0.609375)
        p.drawString(260, 800, 'CV')
        p.line(0, 780, 1000, 780)
        p.line(0, 778, 1000, 778)
        x1 = 20
        y1 = 750

        # RENDER DATA
        for i, j in data.items():
            p.setFont('Helvetica', 15, leading=None)
            p.drawString(x1, y1 - 12, f'{i}')
            p.setFont('Helvetica', 10, leading=None)
            p.drawString(x1, y1 - 20, f'{j}')
            y1 -= 60

        p.setTitle(f'report-{self.id}')
        p.save()

        # pdf_done = buffer.getvalue()
        # buffer.close()
        # file_data = ContentFile(pdf_done)

        buffer.seek(0)
        new_pdf = PdfFileReader(buffer)
        output = PdfFileWriter()
        page = new_pdf.getPage(0)
        output.addPage(page)

        pdf_bytes = BytesIO()
        output.write(pdf_bytes)

        self.pdf = pdf_bytes
        super(Profile, self).save(*args,**kwargs)

    def __str__(self):
        self.name

    class Meta:
        db_table = 'MAE_PROFILE'
