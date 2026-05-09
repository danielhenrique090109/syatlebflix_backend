from django.db import models


class Categoria(models.Model):
    """Gêneros/categorias do conteúdo: Ação, Drama, Comédia..."""
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nome']


class Conteudo(models.Model):
    """Representa um filme ou série na plataforma."""

    class Tipo(models.TextChoices):
        FILME = 'filme', 'Filme'
        SERIE = 'serie', 'Série'

    titulo = models.CharField(max_length=200)
    tipo = models.CharField(max_length=10, choices=Tipo.choices)
    descricao = models.TextField()
    ano_lancamento = models.IntegerField()
    categorias = models.ManyToManyField(Categoria, related_name='conteudos')
    url_video = models.URLField(help_text='URL do vídeo (YouTube, CDN, etc.)')
    destaque = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.titulo} ({self.get_tipo_display()})'

    class Meta:
        verbose_name = 'Conteúdo'
        verbose_name_plural = 'Conteúdos'
        ordering = ['-criado_em']

# Create your models here.
