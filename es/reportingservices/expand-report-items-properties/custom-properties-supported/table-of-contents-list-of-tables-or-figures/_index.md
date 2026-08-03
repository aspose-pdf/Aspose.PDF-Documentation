---
title: Tabla de Contenidos Lista de Tablas o Figuras
linktitle: Tabla de Contenidos Lista de Tablas o Figuras
type: docs
weight: 10
url: /reportingservices/table-of-contents-list-of-tables-or-figures/
description: Aprenda a agregar una tabla de contenido, una lista de tablas o figuras en informes PDF usando Aspose.PDF para Reporting Services.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Report Designer no admite la adición de tablas de contenido para documentos de informes. Con Aspose.PDF para Reporting Services, puede indicar fácilmente al renderizado de PDF que produzca documentos PDF con tabla de contenido o lista de tablas o figuras. Puedes hacerlo en los siguientes pasos:

{{% /alert %}}

Asegúrese de que el archivo Aspose.Pdf.ListSectionStyle.xml exista en el directorio ```<Instance>```/bin, where ```<Instance>``` is the directory of the Report Server. If the file does not exist, create it in the ```<Instance>```/bin y coloque el siguiente marcado dentro.

## Tabla de contenido

### Ejemplo

```cs
<ListSection ListType="TableOfContents">
              <Title Alignment="Center">
            <Segment IsTrueTypeFontBold="true" FontSize="30">TableOfContents</Segment>
              </Title>
              <ListLevelFormat Level="1" LeftMargin="0">
            <TextInfo IsTrueTypeFontBold="true" IsTrueTypeFontItalic="true"></TextInfo>
              </ListLevelFormat>
              <ListLevelFormat Level="2" LeftMargin="10">
            <TextInfo IsUnderline="true" FontSize="10"></TextInfo>
              </ListLevelFormat>
              <ListLevelFormat Level="3" LeftMargin="20">
            <TextInfo IsTrueTypeFontBold="true"></TextInfo>
              </ListLevelFormat>
              <ListLevelFormat Level="4" LeftMargin="30">
            <TextInfo IsTrueTypeFontBold="true"></TextInfo>
              </ListLevelFormat>
</ListSection>
```

##  Lista de tablas

### Ejemplo

```cs
<ListSection ListType="ListOfTables">
              <Title>
            <Segment IsTrueTypeFontBold="true" FontSize="30">ListOfTables</Segment>
              </Title>
</ListSection>
```

## Lista de figuras

### Ejemplo

```cs
 <ListSection ListType="ListOfFigures">
    <Title>
            <Segment IsTrueTypeFontBold="true" FontSize="30">ListOfFigures</Segment>
    </Title>
</ListSection>

```

Consulte la sección 'Trabajar con TOC' de la documentación en línea de Aspose.Pdf.

**2-** Agregue el parámetro de informe `IsListSectionSupported` y establezca el valor en Verdadero como se muestra en el párrafo `List Section`.
**3-** Agregue una propiedad personalizada para el elemento de su informe que desea que aparezca en la Tabla de contenido, Lista de tablas o Figuras.

```text
Custom Property Name: IsInList
Property Value: Boolean
Custom Property Value: True or False
```

Marca el elemento del informe actual según el índice de la tabla de contenido o de la lista de tablas o figuras.

```text
Custom Property Name: Title
Custom Property Type: String
```

El título del elemento que se muestra en la tabla de contenido, lista de tablas o figuras.

```text
Custom Property Name: ListLevel
Custom Property Type: Integer
```

El nivel de los elementos enumerados que se muestran en la tabla de contenido.
