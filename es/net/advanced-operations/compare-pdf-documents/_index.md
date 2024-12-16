---
title: Comparar documentos PDF
linktitle: Comparar PDF
type: docs
weight: 180
url: /es/net/compare-pdf-documents/
description: Desde la versión 24.7 es posible comparar el contenido de documentos PDF con marcas de anotación y salida lado a lado
lastmod: "2024-08-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Comparando documentos PDF con Aspose.PDF para .NET

Al trabajar con documentos PDF, hay momentos en los que necesitas comparar el contenido de dos documentos para identificar diferencias. La biblioteca Aspose.PDF para .NET proporciona un conjunto de herramientas poderoso para este propósito. En este artículo, exploraremos cómo comparar documentos PDF utilizando un par de fragmentos de código simples.

La funcionalidad de comparación en Aspose.PDF te permite comparar dos documentos PDF página por página. Puedes elegir comparar páginas específicas o documentos completos. El documento de comparación resultante resalta las diferencias, facilitando la identificación de cambios entre los dos archivos.

### Comparando páginas específicas

El primer fragmento de código demuestra cómo comparar las primeras páginas de dos documentos PDF.

# Comparación de las Primeras Páginas de Dos Documentos PDF

## Pasos:

1. Inicialización del Documento.
El código comienza inicializando dos documentos PDF utilizando sus respectivas rutas de archivo (documentPath1 y documentPath2). Las rutas se especifican como cadenas vacías por ahora, pero en la práctica, deberías reemplazarlas con las rutas de archivo reales.

2. Proceso de Comparación.
   - Selección de Página - la comparación se limita a la primera página de cada documento ('Pages[1]').
   - Opciones de Comparación:

   'AdditionalChangeMarks = true' - esta opción asegura que se muestren marcadores de cambio adicionales. Estos marcadores destacan las diferencias que podrían estar presentes en otras páginas, incluso si no están en la página actual que se está comparando.

   'ComparisonMode = ComparisonMode.IgnoreSpaces' - este modo indica al comparador que ignore los espacios en el texto, centrándose solo en los cambios dentro de las palabras.

3.
```
```cs
    string documentPath1 = "";
    string documentPath2= "";

    string resultPdfPath ="";

    using (Document document1 = new Document(documentPath1), document2 = new Document(documentPath2))
    {
        SideBySidePdfComparer.Compare(document1.Pages[1], document2.Pages[1], resultPdfPath, new SideBySideComparisonOptions()
        {
            AdditionalChangeMarks = true,
            ComparisonMode = ComparisonMode.IgnoreSpaces
        });
    }
```


### Comparando Documentos Completos

El segundo fragmento de código amplía el alcance para comparar el contenido completo de dos documentos PDF.

Pasos:

1. Inicialización del Documento.
Al igual que en el primer ejemplo, se inicializan dos documentos PDF con sus rutas de archivo.
2. Proceso de Comparación.
- Comparación de Documento Completo - a diferencia del primer fragmento, este código compara el contenido completo de los dos documentos.
- Opciones de Comparación - las opciones son las mismas que en el primer fragmento, asegurando que los espacios se ignoren y se muestren marcadores de cambio adicionales.

3.
```cs
    string documentPath1 = "";
    string documentPath2 = "";

    string resultPdfPath ="";

    using (Document document1 = new Document(documentPath1), document2 = new Document(documentPath2))
    {
        SideBySidePdfComparer.Compare(document1, document2, resultPdfPath, new SideBySideComparisonOptions()
        {
            AdditionalChangeMarks = true,
            ComparisonMode = ComparisonMode.IgnoreSpaces
        });
    }
```

Los resultados de la comparación generados por estos fragmentos son documentos PDF que puedes abrir en un visor como Adobe Acrobat. Si utilizas la vista de dos páginas en Adobe Acrobat, verás los cambios uno al lado del otro:

- Eliminaciones - se señalan en la página izquierda.
- Inserciones - se señalan en la página derecha.

Al configurar 'AdditionalChangeMarks' en 'true', también puedes ver marcadores para cambios que pueden ocurrir en otras páginas, incluso si esos cambios no están en la página actual que se está viendo.

**Aspose.PDF for .NET** proporciona herramientas robustas para comparar documentos PDF, ya sea que necesites comparar páginas específicas o documentos completos.
**Aspose.PDF para .NET** proporciona herramientas robustas para comparar documentos PDF, ya sea que necesite comparar páginas específicas o documentos enteros.
