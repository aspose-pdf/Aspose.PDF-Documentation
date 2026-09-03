---
title: Administrar encabezados y pies de página de PDF usando Java
linktitle: Administrar encabezados y pies de página de PDF
type: docs
weight: 70
url: /es/java/artifacts-header-footer/
description: Aprenda cómo agregar y eliminar artefactos de encabezado y pie de página en documentos PDF usando Aspose.PDF for Java.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo agregar, personalizar y eliminar encabezados y pies de página de PDF usando Java
Abstract: Este artículo explica cómo administrar los artefactos de encabezado y pie de página en documentos PDF utilizando Aspose.PDF for Java. Cubre la creación de objetos reutilizables `HeaderArtifact` y `FooterArtifact` con estado de texto y alineación personalizados, su adición a una página y la eliminación de los artefactos de encabezado y pie de página existentes.
---
Los artefactos de encabezado y pie de página son elementos de paginación sin contenido que se utilizan comúnmente para etiquetas repetidas, identificadores de página y encuadre del diseño.

## Crear un artefacto de encabezado

Utilice este asistente cuando necesite un artefacto de encabezado reutilizable con estilo de texto y alineación consistentes.

1. Crear un [HeaderArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerartifact/).
1. Establezca su texto, configuraciones de Font y color de primer plano.
1. Configure la alineación horizontal y devuelva el artifact.

```java
public static HeaderArtifact createHeaderArtifact(String text) {
    HeaderArtifact artifact = new HeaderArtifact();
    artifact.setText(text);
    artifact.getTextState().setFontSize(14);
    artifact.getTextState().setFont(FontRepository.findFont("Arial"));
    artifact.getTextState().setForegroundColor(Color.getNavy());
    artifact.setArtifactHorizontalAlignment(HorizontalAlignment.Center);
    return artifact;
}
```

## Crear un artifact de pie de página

Este asistente crea un artifact de pie de página reutilizable con el mismo patrón de estilo que el artifact de encabezado.

1. Crear un [FooterArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/footerartifact/).
1. Establezca su texto, estado del texto y color de primer plano.
1. Configure la alineación y devuelva el artefacto.

```java
public static FooterArtifact createFooterArtifact(String text) {
    FooterArtifact artifact = new FooterArtifact();
    artifact.setText(text);
    artifact.getTextState().setFontSize(14);
    artifact.getTextState().setFont(FontRepository.findFont("Arial"));
    artifact.getTextState().setForegroundColor(Color.getNavy());
    artifact.setArtifactHorizontalAlignment(HorizontalAlignment.Center);
    return artifact;
}
```

## Agregar un artefacto de encabezado

Utilice este ejemplo cuando una página deba mostrar un artefacto de encabezado reutilizable.

1. Abrir el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cree el artefacto de encabezado mediante el método auxiliar.
1. Agregue el artefacto a la página y guarde el archivo de salida.

```java
public static void addHeaderArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HeaderArtifact header = createHeaderArtifact("Sample Header");
        document.getPages().get_Item(1).getArtifacts().add(header);
        document.save(outputFile.toString());
    }
}
```

## Agregar un artefacto de pie de página

Utilice este ejemplo cuando la página debe mostrar un artefacto de pie de página con formato reutilizable.

1. Abrir el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cree el artefacto de pie de página mediante el método auxiliar.
1. Agregue el artefacto a la página y guarde el archivo de salida.

```java
public static void addFooterArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        FooterArtifact footer = createFooterArtifact("Sample Footer");
        document.getPages().get_Item(1).getArtifacts().add(footer);
        document.save(outputFile.toString());
    }
}
```

## Eliminar artefactos de encabezado y pie de página

Utilice este método cuando los artefactos de encabezado y pie de página existentes deban eliminarse de la página.

1. Abrir el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterar a través de la colección de artefactos de página en orden inverso.
1. Elimina los artefactos de paginación cuyo subtipo es encabezado o pie de página, luego guarda el documento.

```java
public static void deleteHeaderFooterArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = document.getPages().get_Item(1).getArtifacts().size(); i >= 1; i--) {
            Artifact artifact = document.getPages().get_Item(1).getArtifacts().get_Item(i);
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && (artifact.getSubtype() == Artifact.ArtifactSubtype.Header
                    || artifact.getSubtype() == Artifact.ArtifactSubtype.Footer)) {
                document.getPages().get_Item(1).getArtifacts().delete(artifact);
            }
        }

        document.save(outputFile.toString());
    }
}
```
