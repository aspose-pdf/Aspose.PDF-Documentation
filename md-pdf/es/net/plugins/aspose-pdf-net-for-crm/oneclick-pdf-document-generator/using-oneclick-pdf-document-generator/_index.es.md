---
title: Uso del generador de documentos PDF OneClick
type: docs
weight: 10
url: /net/using-oneclick-pdf-document-generator/
description: Aprende a utilizar el generador de documentos PDF OneClick de Aspose.PDF en Microsoft Dynamics
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Crear plantilla y agregar en CRM

- Abre Word y crea una plantilla.
- Inserta campos MailMerge para datos provenientes del CRM.

![Insertar campos MailMerge](using-oneclick-pdf-document-generator_1.png)

- Asegúrate de que el nombre del campo coincida exactamente con el campo del CRM.
- Las plantillas son específicas para usar con cada entidad individual.

![Plantilla de demostración](using-oneclick-pdf-document-generator_2.png)

- Una vez creada la plantilla, abre la entidad de configuración de PDF OneClick en CRM y crea un nuevo registro.
- Da el nombre de la plantilla, selecciona la entidad para la que está definida la plantilla y adjunta el documento creado en el adjunto.

![Seleccionar Plantilla](using-oneclick-pdf-document-generator_3.png)

## Generar documento desde el botón de la cinta

- Abre el registro donde deseas generar el documento.
- Abra el Registro donde desea generar el documento.
- Haga clic en el botón OneClick PDF en la cinta de opciones.

![Haga clic en OneClick PDF](using-oneclick-pdf-document-generator_4.png)

- Desde la ventana emergente: Seleccione plantilla, Nombre de archivo y Acción y haga clic en Generar.
- Verifique el archivo descargado o las Notas, según la selección.

## Configurar botones OneClick y usarlos

- Para usar el botón OneClick directamente desde el Formulario, abra la Personalización del Formulario.
- Inserte WebResource donde desee agregar botones OneClick.
- Seleccione OpenButtonPage en Webresource y asígnele un Nombre.
- Configure los botones en el campo de Datos en el siguiente ejemplo.

![Propiedades de WebResource](using-oneclick-pdf-document-generator_5.png)

- Use una línea separada para cada botón y utilice la siguiente sintaxis:
  - Sintaxis: Nombre de la plantilla |<Acción: Descargar/Nota>|Nombre del archivo de salida
  - Ejemplo: Demo|Descargar|Mi archivo descargado
- Guarde y publique la personalización.
- El botón está disponible en el formulario.

![El botón está disponible en el formulario](using-oneclick-pdf-document-generator_6.png)
![El botón está disponible en el formulario](using-oneclick-pdf-document-generator_6.png)
