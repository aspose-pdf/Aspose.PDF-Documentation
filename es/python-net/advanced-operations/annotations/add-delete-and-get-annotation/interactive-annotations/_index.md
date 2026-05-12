---
title: Anotaciones interactivas usando Python
linktitle: Anotaciones interactivas
type: docs
weight: 60
url: /es/python-net/interactive-annotations/
description: Aprenda cómo agregar, leer y eliminar anotaciones de enlace, y cómo crear botones de navegación e impresión en documentos PDF usando Aspose.PDF for Python via .NET.
lastmod: "2026-04-21"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Trabaja con anotaciones interactivas de PDF y botones en Python.
Abstract: Este artículo explica cómo trabajar con anotaciones interactivas en archivos PDF usando Aspose.PDF for Python via .NET. Cubre la adición de anotaciones de enlace, la lectura de áreas de enlace existentes, la eliminación de anotaciones de enlace, la creación de botones de navegación de página y la incorporación de un botón de impresión a un documento PDF.
---

Este artículo muestra cómo trabajar con anotaciones interactivas en documentos PDF utilizando Aspose.PDF for Python via .NET.

El script de ejemplo muestra varios flujos de trabajo comunes:

- agregar una anotación de enlace al texto existente
- obtener los rectángulos de anotación de enlace de una página
- eliminar anotaciones de enlace
- crear botones de navegación
- crear un botón de impresión

## Anotación de enlace

### Agregar anotación de enlace

Este ejemplo busca en la primera página el fragmento de texto `"file"` y coloca una anotación de enlace clicable sobre el área de texto coincidente. Cuando el usuario hace clic en la anotación, el PDF abre la dirección web especificada.

#### Cargue el documento y encuentre el texto objetivo

Crear una `Document` objeto y usar `TextFragmentAbsorber` buscar el texto que se volverá interactivo.

```python
document = ap.Document(infile)
text_fragment_absorber = ap.text.TextFragmentAbsorber("file")

document.pages[1].accept(text_fragment_absorber)
phone_number_fragment = text_fragment_absorber.text_fragments[1]
```

#### Crear la anotación de enlace

Construir un `LinkAnnotation` usando el rectángulo del fragmento de texto coincidente y asignar una acción URI a él.

```python
link_annotation = ap.annotations.LinkAnnotation(
    document.pages[1], phone_number_fragment.rectangle
)
link_annotation.action = ap.annotations.GoToURIAction("https://www.aspose.com")
```

#### Añade la anotación y guarda el PDF

Agregue la anotación a la página y guarde el archivo actualizado.

```python
document.pages[1].annotations.append(link_annotation)
document.save(outfile)
```

#### Ejemplo completo

```python
def link_add(infile, outfile):
    document = ap.Document(infile)
    text_fragment_absorber = ap.text.TextFragmentAbsorber("file")

    document.pages[1].accept(text_fragment_absorber)
    phone_number_fragment = text_fragment_absorber.text_fragments[1]

    link_annotation = ap.annotations.LinkAnnotation(
        document.pages[1], phone_number_fragment.rectangle
    )
    link_annotation.action = ap.annotations.GoToURIAction("https://www.aspose.com")

    document.pages[1].annotations.append(link_annotation)
    document.save(outfile)
```

### Obtener anotación de enlace

Para inspeccionar los enlaces interactivos existentes, filtre la colección de anotaciones en la primera página y conserve solo los elementos cuyo tipo es `LINK`. La muestra luego imprime el rectángulo para cada anotación coincidente.

#### Cargar el PDF y recopilar anotaciones de enlace

```python
document = ap.Document(infile)
link_annotations = [
    a
    for a in document.pages[1].annotations
    if (a.annotation_type == ap.annotations.AnnotationType.LINK)
]
```

#### Leer los rectángulos de anotación

Recorra las anotaciones filtradas y muestre las coordenadas de cada área de enlace.

```python
for link_annotation in link_annotations:
    print(link_annotation.rect)
```

#### Ejemplo completo

```python
def link_get(infile, outfile):
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for link_annotation in link_annotations:
        print(link_annotation.rect)
```

### Eliminar anotación de enlace

Este flujo de trabajo elimina todas las anotaciones de enlaces de la primera página y guarda el PDF limpio como un nuevo archivo.

#### Encuentra las anotaciones de enlace para eliminar

```python
document = ap.Document(infile)
link_annotations = [
    a
    for a in document.pages[1].annotations
    if (a.annotation_type == ap.annotations.AnnotationType.LINK)
]
```

#### Eliminar cada anotación de enlace

```python
for link_annotation in link_annotations:
    document.pages[1].annotations.delete(link_annotation)
```

#### Guardar el documento actualizado

```python
document.save(outfile)
```

#### Ejemplo completo

```python
def link_delete(infile, outfile):
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for link_annotation in link_annotations:
        document.pages[1].annotations.delete(link_annotation)

    document.save(outfile)
```

## Anotación de widget

### Agregar botón de navegación

Los botones de navegación son útiles en PDFs de varias páginas cuando deseas que los lectores se desplacen entre páginas sin usar la interfaz del visor. Este ejemplo agrega `Previous Page` y `Next Page` botones a cada página.

#### Definir configuración del botón

Almacena los textos de los botones, sus posiciones y acciones predefinidas en una lista de configuración simple.

```python
button_config = [
    ("Previous Page", 120.0, ap.annotations.PredefinedAction.PREV_PAGE),
    ("Next Page", 230.0, ap.annotations.PredefinedAction.NEXT_PAGE),
]
```

#### Cargue el PDF y asegúrese de que existan varias páginas

El ejemplo abre el documento fuente y agrega una página más para que las acciones de navegación tengan al menos dos páginas con las que trabajar.

```python
document = ap.Document(infile)
document.pages.add()
```

#### Cree los botones en cada página

Para cada página, crea un `ButtonField`, establezca su texto y colores, asigne una acción de navegación predefinida y agréguelo al formulario.

```python
for page in document.pages:
    for name, x_pos, action in button_config:
        rect = ap.Rectangle(x_pos, 10.0, x_pos + 100, 40.0, True)
        button = ap.forms.ButtonField(page, rect)
        button.partial_name = name
        button.value = name
        button.characteristics.border = ap.Color.red.to_rgb()
        button.characteristics.background = ap.Color.orange.to_rgb()
        button.actions.on_release_mouse_btn = ap.annotations.NamedAction(action)
        document.form.add(button)
```

#### Guardar el resultado

```python
document.save(outfile)
```

#### Ejemplo completo

```python
def navigation_buttons_add(infile, outfile):
    button_config = [
        ("Previous Page", 120.0, ap.annotations.PredefinedAction.PREV_PAGE),
        ("Next Page", 230.0, ap.annotations.PredefinedAction.NEXT_PAGE),
    ]

    document = ap.Document(infile)
    document.pages.add()

    for page in document.pages:
        for name, x_pos, action in button_config:
            rect = ap.Rectangle(x_pos, 10.0, x_pos + 100, 40.0, True)
            button = ap.forms.ButtonField(page, rect)
            button.partial_name = name
            button.value = name
            button.characteristics.border = ap.Color.red.to_rgb()
            button.characteristics.background = ap.Color.orange.to_rgb()
            button.actions.on_release_mouse_btn = ap.annotations.NamedAction(action)
            document.form.add(button)

    document.save(outfile)
```

### Agregar botón de impresión

Este ejemplo crea un PDF de una sola página y coloca un botón de impresión cerca de la parte superior de la página. Al hacer clic en el botón se activa la acción de impresión predefinida en un visor de PDF compatible.

#### Crear un nuevo PDF y añadir una página

```python
document = ap.Document()
page = document.pages.add()
```

#### Crear y configurar el botón

Definir el rectángulo del botón, crear el `ButtonField`, establezca su leyenda y adjunte la acción de impresión.

```python
rect = ap.Rectangle(72, 748, 164, 768, True)

print_button = ap.forms.ButtonField(page, rect)
print_button.alternate_name = "Print current document"
print_button.color = ap.Color.black
print_button.partial_name = "printBtn1"
print_button.value = "Print Document"
print_button.actions.on_release_mouse_btn = ap.annotations.NamedAction(
    ap.annotations.PredefinedAction.FILE_PRINT
)
```

#### Establecer estilos de borde y fondo

El ejemplo define un borde sólido y aplica colores personalizados para hacer que el botón sea visible en el documento.

```python
border = ap.annotations.Border(print_button)
border.style = ap.annotations.BorderStyle.SOLID
border.width = 2
print_button.border = border

print_button.characteristics.border = ap.Color.blue.to_rgb()
print_button.characteristics.background = ap.Color.light_blue.to_rgb()
```

#### Añade el botón y guarda el PDF

```python
document.form.add(print_button)
document.save(outfile)
```

#### Ejemplo completo

```python
def print_button_add(infile, outfile):
    document = ap.Document()
    page = document.pages.add()

    rect = ap.Rectangle(72, 748, 164, 768, True)

    print_button = ap.forms.ButtonField(page, rect)
    print_button.alternate_name = "Print current document"
    print_button.color = ap.Color.black
    print_button.partial_name = "printBtn1"
    print_button.value = "Print Document"
    print_button.actions.on_release_mouse_btn = ap.annotations.NamedAction(
        ap.annotations.PredefinedAction.FILE_PRINT
    )

    border = ap.annotations.Border(print_button)
    border.style = ap.annotations.BorderStyle.SOLID
    border.width = 2
    print_button.border = border

    print_button.characteristics.border = ap.Color.blue.to_rgb()
    print_button.characteristics.background = ap.Color.light_blue.to_rgb()

    document.form.add(print_button)
    document.save(outfile)
```

## Temas relacionados

- [Importar y exportar anotaciones](/python-net/import-export-annotations/)
- [Anotaciones de marcado](/python-net/markup-annotations/)
- [Anotaciones de medios](/python-net/media-annotations/)
- [Anotaciones de Seguridad](/python-net/security-annotations/)
- [Anotaciones de forma](/python-net/shape-annotations/)
- [Anotaciones basadas en texto](/python-net/text-based-Annotations/)
- [Anotaciones de Marca de Agua](/python-net/watermark-annotations/)
