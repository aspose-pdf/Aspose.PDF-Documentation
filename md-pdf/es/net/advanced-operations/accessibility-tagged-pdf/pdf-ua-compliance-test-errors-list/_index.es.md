---
title: Prueba de Cumplimiento PDF-UA - Lista de Errores
linktitle: Prueba de Cumplimiento PDF-UA - Lista de Errores
type: docs
weight: 50
url: /net/pdf-ua-compliance-test-errors-list/
description: Este artículo muestra una lista de los errores que pueden surgir durante la prueba de cumplimiento PDF/UA usando la API de Aspose.PDF y C# o VB.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Prueba de Cumplimiento PDF-UA - Lista de Errores",
    "alternativeHeadline": "Pruebas de cumplimiento PDF/UA utilizando la API",
    "author": {
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, generación de documentos",
    "wordcount": "302",
    "proficiencyLevel":"Principiante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipo de Documentación de Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "ventas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventas",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/pdf-ua-compliance-test-errors-list/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/pdf-ua-compliance-test-errors-list/"
    },
    "dateModified": "2022-02-04",
    "description": "Este artículo muestra una lista de los errores que pueden surgir durante la prueba de cumplimiento PDF/UA usando la API de Aspose.PDF y C# o VB."
}
</script>
Mientras realiza pruebas de cumplimiento PDF/UA utilizando la API de Aspose.PDF, puede interesarle conocer los mensajes de error que puede obtener. Estos errores son de diferentes tipos como General, Texto, Fuentes, Encabezados y varios otros. La información sobre estos errores puede ser útil para conocer la causa exacta de los errores y su manejo.

En este artículo, enumeramos los errores que pueden surgir durante las pruebas de cumplimiento PDF/UA utilizando la API.

## **General**

|**Code**|**Severity**|**Message**|
| :- | :- | :- |
|5:1|Error|Identificador PDF/UA ausente|
|6.2:1.1|Error|Árbol de padres estructural: Entrada inconsistente encontrada|
|7.1:1.1(14.8.1)|Error|El documento no está marcado como etiquetado|
|7.1:1.1(14.8)|Error|Objeto [OBJECT_NAME] no etiquetado|
|7.1:1.2(14.8.2.2)|Error|Artefacto presente dentro del contenido etiquetado|
|7.1:1.3(14.8.2.2)|Error|Contenido etiquetado presente dentro de un artefacto|
|7.1:2.1|Advertencia|Árbol de estructura ausente|
|7.1:2.2|Advertencia|Elemento de estructura ‘Document’ encontrado que no es un elemento raíz|
|7.1:2.3|Advertencia|Elemento de estructura ‘[ELEMENT_NAME]’ utilizado como elemento raíz|
```
|7.1:2.3|Advertencia|El elemento de estructura ‘[ELEMENT_NAME]’ utilizado como elemento raíz|
|7.1:2.4.1|Advertencia|Uso posiblemente inapropiado de un elemento de estructura ‘[ELEMENT_NAME]’|
|7.1:2.4.2|Error|Uso inválido de un elemento de estructura ‘[ELEMENT_NAME]’|
|7.1:2.5|Advertencia|Elemento de estructura ‘[ELEMENT_NAME]’ anidado incorrectamente en StructTreeRoot|
|7.1:3(14.8.4)|Error|Tipo de estructura no estándar ‘[TYPE_NAME]’ no está mapeado a un tipo de estructura estándar ni a otro tipo de estructura no estándar|
|7.1:4(14.8.4)|Advertencia|Tipo de estructura estándar ‘[TYPE_NAME]’ remapeado a ‘[TYPE_NAME]’|
|7.1:5|Necesita revisión manual|Contraste de color|
|7.1:6.1|Error|Falta metadatos XMP en el documento|
|7.1:6.2|Error|Falta el título en los metadatos XMP del documento|
|7.1:6.3|Advertencia|El título está vacío en los metadatos XMP del documento|
|7.1:7.1(12.2)|Advertencia|Falta el diccionario ‘ViewerPreferences’|
|7.1:7.2(12.2)|Error|La entrada ‘DisplayDocTitle’ no está establecida|
|7.1:8(14.7.1)|Error|La entrada ‘Suspects’ está establecida|
|7.1:9.1(14.7)|Error|Falta la clave ‘StructParents’ en la página|
|7.1:9.2(14.7)|Error|Falta la entrada ‘StructParent’ en la anotación|
```
|7.1:9.2(14.7)|Error|Falta la entrada 'StructParent' en la anotación|
|7.1:9.3(14.7)|Error|No se encontró la entrada para los 'StructParents' dados|

## **Texto**

|**Código**|**Severidad**|**Mensaje**|
| :- | :- | :- |
|7.2:1|Necesita revisión manual|Orden de lectura lógico|
|7.2:2(14.8.2.4.2)|Error|Los caracteres en un objeto de texto no pueden ser mapeados a Unicode|
|7.2:3.1(14.9.2.2)|Error|No se puede determinar el idioma natural para el objeto de texto|
|7.2:3.2(14.9.2.2)|Error|No se puede determinar el idioma natural del texto alternativo|
|7.2:3.3(14.9.2.2)|Error|No se puede determinar el idioma natural del texto real|
|7.2:3.4(14.9.2.2)|Error|No se puede determinar el idioma natural del texto de expansión|
|7.2:4(14.9.4)|Error|Carácter extensible no etiquetado usando ActualText|

## **Fuentes**

|**Cláusula**|**Severidad**|**Mensaje**|
| :- | :- | :- |
|7.21.3.1|Error|La colección de caracteres en CIDFont no es compatible con la colección de caracteres del CMap interno|
|7.21.3.2|Error|CIDToGIDMap no está incrustado o está incompleto en la fuente ‘[FONT_NAME]’|
|7.21.3.2|Error|CMap no está incrustado para la fuente ‘[FONT_NAME]’|
|7.21.3.2|Error|CMap no está incrustado para la fuente ‘[FONT_NAME]’|
|7.21.4.2|Error|Falta CIDSet o está incompleto para la fuente ‘[FONT_NAME]’|
|7.21.4.2|Error|Faltan glifos en la fuente incrustada ‘[FONT_NAME]’|
|7.21.6|Error|La fuente TrueType no simbólica ‘[FONT_NAME]’ no tiene entradas cmap|
|7.21.6|Error|Entrada de codificación prohibida para la fuente TrueType simbólica ‘[FONT_NAME]’|
|7.21.6|Error|Se utiliza una codificación incorrecta para la fuente TrueType ‘[FONT_NAME]’|
|7.21.6|Error|Array “Differences” incorrecto para la fuente TrueType no simbólica ‘[FONT_NAME]’|

## **Gráficos**

|**Código**|**Severidad**|**Mensaje**|
| :- | :- | :- |
|7.3:1(14.8.4.5)|Error|El elemento ‘[ELEMENT_NAME]’ en una sola página sin cuadro delimitador|
|7.3:2|Error|Falta texto alternativo para el elemento estructural ‘[ELEMENT_NAME]’|
|7.3:3|Error|Falta la leyenda que acompaña a la figura|
|7.3:4(14.8.4.5)|Error|El objeto gráfico aparece entre los operadores BT y ET|

## **Encabezados**

|**Código**|**Severidad**|**Mensaje**|
| :- | :- | :- |
|7.4.2:1|Error|El primer encabezado no está en el primer nivel|
|7.4.2:2|Error|El encabezado numerado omite uno o más niveles de encabezado|
|7.4.2:2|Error|Se omite uno o más niveles en los títulos numerados|
|7.4.4:1|Error|Se encontraron elementos de estructura ‘H’ y ‘Hn’|
|7.4.4:2|Error|Más de un elemento de estructura ‘H’ dentro del elemento de estructura padre|

## **Tablas**

|**Code**|**Severity**|**Message**|
| :- | :- | :- |
|7.5:1|Warning|Fila de tabla irregular|
|7.5:2|Error|La celda de encabezado de la tabla no tiene subceldas asociadas|
|7.5:3.1|Warning|Faltan encabezados de tabla|
|7.5:3.2|Warning|Falta resumen de la tabla|

## **Listas**

|**Code**|**Severity**|**Message**|
| :- | :- | :- |
|7.6:1|Error|El elemento de estructura ‘LI’ debe ser hijo del elemento ‘L’|
|7.6:2|Error|Los elementos de estructura ‘Lbl’ y ‘LBody’ deben ser hijos del elemento ‘LI’|

## **Notas y referencias**

|**Code**|**Severity**|**Message**|
| :- | :- | :- |
|7.9:2.1|Error|Falta ID en el elemento de estructura ‘Note’|
|7.9:2.2|Error|La entrada de ID en el elemento de estructura ‘Note’ no es única|

## **Contenido opcional**

|**Code**|**Severity**|**Message**|
| :- | :- | :- |
|7.10:1|Error|Falta ‘Name’ en el diccionario de configuración de contenido opcional|
|7.10:1|Error|Falta ‘Name’ en el diccionario de configuración de contenido opcional|
|7.10:2|Error|El diccionario de configuración de contenido opcional contiene la clave ‘AS’|

## **Archivos embebidos**

|**Código**|**Severidad**|**Mensaje**|
| :- | :- | :- |
|7.11:1|Error|Falta la clave ‘F’ o ‘UF’ en la especificación del archivo|
|7.11:2|Advertencia|Falta la clave ‘Desc’ en la especificación del archivo|

## **Firmas digitales**

|**Código**|**Severidad**|**Mensaje**|
| :- | :- | :- |
|7.13:1|Error|El campo de firma ‘[FIELD_NAME]’ no se ajusta a la especificación|
|7.13:2.1|Error|No se puede determinar el idioma natural de un nombre alternativo de un campo de formulario ‘[FIELD_NAME]’|
|7.13:2.2|Error|Falta la entrada de nombre de campo alternativo en el campo de formulario ‘[FIELD_NAME]’|

## **Formularios no interactivos**

|**Código**|**Severidad**|**Mensaje**|
| :- | :- | :- |
|7.14:1|Error|Falta el atributo ‘PrintField’ en el elemento de formulario no interactivo|

## **XFA**

|**Código**|**Severidad**|**Mensaje**|
| :- | :- | :- |
|7.15:1|Error|El PDF contiene un formulario XFA dinámico|

## **Seguridad**

|**Código**|**Severidad**|**Mensaje**|
|**Code**|**Severity**|**Message**|
| :- | :- | :- |
|7.16:1(7.6.3.2)|Error|La configuración de seguridad impide que las tecnologías asistivas accedan al contenido del documento|
|7.16:2(7.6.3.2)|Error|La conversión no está permitida por restricciones de permiso|

## **Navigation**

|**Code**|**Severity**|**Message**|
| :- | :- | :- |
|7.17:1|Error|Error en los contornos del documento|
|7.17:2|Error|No se puede determinar el lenguaje natural de los contornos|
|7.17:3|Need manual check|Etiquetas de página semánticamente apropiadas|

## **Annotations**

|**Code**|**Severity**|**Message**|
| :- | :- | :- |
|7.18.1:1|Error|No se puede determinar el lenguaje natural de la entrada de Contenidos|
|7.18.1:2|Error|Falta descripción alternativa para una anotación|
|7.18.1:3|Error|La anotación no está anidada dentro de un elemento estructural ‘Annot’|
|7.18.2:1|Error|Una anotación con subtipo no definido en ISO 32000 no cumple con 7.18.1|
|7.18.2:2|Error|Existe una anotación del subtipo TrapNet|
|7.18.3:1|Error|La entrada de orden de tabulación en página con anotaciones no está establecida en 'S' (Estructura)|
|7.18.4:1|Error|La anotación ‘Widget’ no está anidada dentro de un elemento estructural ‘Form’|
|7.18.4:1|Error|La anotación 'Widget' no está anidada dentro de un elemento de estructura 'Form'|
|7.18.5:1|Error|La anotación 'Link' no está anidada dentro de un elemento de estructura 'Link'|
|7.18.6.2:1|Error|Falta la clave CT en el diccionario de datos del clip de medios|
|7.18.6.2:2|Error|Falta la clave Alt en el diccionario de datos del clip de medios|
|7.18.7:1|Error|Anotación de adjunto de archivo. Falta la clave 'F' o 'UF' en la especificación del archivo|
|7.18.7:2|Warning|Anotación de adjunto de archivo. Falta la clave 'Desc' en la especificación del archivo|
|7.18.8:1|Error|Se incluye una anotación PrinterMark en la estructura lógica|
|7.18.8:2|Error|El flujo de apariencia de una anotación PrinterMark no está marcado como Artefacto|

## **Actions**

|**Code**|**Severity**|**Message**|
| :- | :- | :- |
|7.19:1|Need check manual|Se encontraron acciones. Necesidad de verificar acciones de acuerdo con la especificación PDF/UA manualmente|

## **XObjects**

|**Code**|**Severity**|**Message**|
| :- | :- | :- |
|7.20:1|Error|No se debe usar XObject de referencia en un archivo PDF/UA conforme|
|7.20:2|Error|El contenido de Form XObject no está incorporado en elementos de estructura|
|7.20:2|Error|El contenido del Form XObject no está incorporado en los elementos estructurales|

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "ventas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventas",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Biblioteca de manipulación de PDF para .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>


