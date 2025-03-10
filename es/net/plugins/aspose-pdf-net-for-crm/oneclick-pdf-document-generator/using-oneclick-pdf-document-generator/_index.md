---
title: Usando el Generador de Documentos PDF OneClick
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /es/net/using-oneclick-pdf-document-generator/
description: Aprende a usar Aspose.PDF OneClick PDF Document Generator en Microsoft Dynamics
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Using OneClick PDF Document Generator",
    "alternativeHeadline": "Streamlined PDF Generation in Microsoft Dynamics",
    "abstract": "Desbloquea la generación de documentos sin problemas en Microsoft Dynamics con el Generador de Documentos PDF OneClick de Aspose.PDF. Esta característica innovadora permite a los usuarios crear plantillas PDF personalizables directamente dentro del CRM, generar documentos de manera eficiente con un solo clic e integrar fácilmente botones OneClick en formularios para un acceso simplificado. Mejora tus capacidades de gestión de datos y aumenta la productividad con esta poderosa herramienta",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "313",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
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
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/using-oneclick-pdf-document-generator/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/using-oneclick-pdf-document-generator/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios avanzados y desarrolladores."
}
</script>

## Crear Plantilla y Agregar en CRM

- Abre Word y crea una plantilla.
- Inserta campos de MailMerge para datos provenientes del CRM.

![Insertar campos de MailMerge](using-oneclick-pdf-document-generator_1.png)

- Asegúrate de que el nombre del campo coincida exactamente con el campo del CRM.
- Las plantillas son específicas para usar con entidades individuales.

![Plantilla de demostración](using-oneclick-pdf-document-generator_2.png)

- Una vez que la plantilla esté creada, abre la entidad de Configuración de PDF OneClick en CRM y crea un nuevo registro.
- Da el nombre de la plantilla, selecciona la entidad para la que se define la plantilla y adjunta el documento creado en el archivo adjunto.

![Seleccionar plantilla](using-oneclick-pdf-document-generator_3.png)

## Generar Documento desde el Botón de la Cinta

- Abre el registro donde deseas generar el documento. (Asegúrate de que ya haya una plantilla adjunta en la configuración para esa entidad)
- Haz clic en el botón OneClick PDF de la cinta.

![Haz clic en OneClick PDF](using-oneclick-pdf-document-generator_4.png)

- Desde el Popup: selecciona plantilla, nombre del archivo y acción y haz clic en Generar.
- Verifica el archivo descargado o notas, según la selección.

## Configurar Botones OneClick y Usarlos

- Para usar el botón OneClick directamente desde el formulario, abre la personalización del formulario.
- Inserta WebResource donde deseas agregar los botones OneClick.
- Selecciona OpenButtonPage en WebResource y dale un nombre.
- Configura los botones en el campo de datos en el siguiente ejemplo.

![Propiedades de WebResource](using-oneclick-pdf-document-generator_5.png)

- Usa una línea separada para cada botón y utiliza la siguiente sintaxis:
  - Sintaxis: Nombre de la plantilla |<Acción: Descargar/Nota>|Nombre del archivo de salida
  - Ejemplo:Demo|Descargar|Mi archivo descargado
- Guarda y publica la personalización.
- El botón está disponible en el formulario.

![El botón está disponible en el formulario](using-oneclick-pdf-document-generator_6.png)