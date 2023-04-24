from django.db import models

# modelo Autor 
class Autor(models.Model):
      nombre= models.CharField(max_length=100)
      
      def __str__(self):
        return self.nombre
      
#modelo Editorial
class Editorial(models.Model):
      nombre =models.CharField(max_length=100)
      
      def __str__(self):
        return self.nombre
      
#modelos Libro
class Libro(models.Model):
      titulo = models.CharField(max_length=100)
      autor = models.ForeignKey(Autor, on_delete=models.CASCADE)      
      editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
      
      def __str__(self):
        return self.titulo
