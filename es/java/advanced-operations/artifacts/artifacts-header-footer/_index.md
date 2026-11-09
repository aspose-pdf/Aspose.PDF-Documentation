---
title: Agregar encabezados y pies de página PDF en Java
linktitle: Agregar encabezados y pies de página
type: docs
weight: 70
url: /es/java/artifacts-header-footer/
description: Crear artefactos de encabezado y pie de página con estilo y agregarlos a las páginas PDF en Java.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar encabezados y pies de página en Java
Abstract: Crear artefactos de encabezado y pie de página con estilo y agregarlos a las páginas PDF en Java.
---
Los artefactos de encabezado y pie de página son elementos de paginación no de contenido que se utilizan comúnmente para etiquetas repetidas, identificadores de página y encuadre de diseño.

## Crear un artefacto de encabezado

Utilice este asistente cuando necesite un artefacto de encabezado reutilizable con estilo de texto y alineación consistentes.

1. Cree un [HeaderArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerartifact/).
1. Establezca su texto, la configuración de la fuente y el color de primer plano.
1. Configure la alineación horizontal y devuelva el artefacto.

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

## Crear un artefacto de pie de página

Este asistente crea un artefacto de pie de página reutilizable con el mismo patrón de estilo que el artefacto de encabezado.

1. Cree un [FooterArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/footerartifact/).
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

Utilice este ejemplo cuando una página debe mostrar un artefacto de encabezado reutilizable.

1. Abra el PDF de origen con [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
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

1. Abra el PDF de origen con [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
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

## Temas relacionados

- [Eliminar encabezados y pies de página](/pdf/es/java/remove-headers-footers/)
- [Trabajar con artefactos PDF en Java](/pdf/es/java/artifacts/)
