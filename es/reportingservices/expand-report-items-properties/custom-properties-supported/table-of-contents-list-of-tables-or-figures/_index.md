---
title: Tabla de contenido Lista de tablas o figuras
linktitle: Tabla de contenido Lista de tablas o figuras
type: docs
weight: 10
url: /es/reportingservices/table-of-contents-list-of-tables-or-figures/
description: Aprenda cómo agregar una tabla de contenido, lista de tablas o figuras en informes PDF usando Aspose.Pdf for Reporting Services.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Report Designer no admite agregar tabla de contenido para documentos de informe. Con Aspose.Pdf for Reporting Services puedes indicar fácilmente al renderizador PDF que produzca documentos PDF con tabla de contenido, o lista de tablas o figuras. Puedes hacerlo en los siguientes pasos:

{{% /alert %}}

{{% alert color="primary" %}}
Asegúrese de que el archivo Aspose.Pdf.ListSectionStyle.xml exista en ```<Instance>```/bin, dónde ```<Instance>``` es el directorio del Report Server. Si el archivo no existe, créalo en el ```<Instance>```directorio /bin y coloque el siguiente marcado dentro.

## Tabla de contenidos

**Ejemplo**

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

##  Lista de Tablas

**Ejemplo**

```cs
<ListSection ListType="ListOfTables">
              <Title>
            <Segment IsTrueTypeFontBold="true" FontSize="30">ListOfTables</Segment>
              </Title>
</ListSection>
```

## Lista de figuras

**Ejemplo**

```cs
 <ListSection ListType="ListOfFigures">
    <Title>
            <Segment IsTrueTypeFontBold="true" FontSize="30">ListOfFigures</Segment>
    </Title>
</ListSection>

```

Consulte la sección 'Working with TOC' de la documentación en línea de Aspose.Pdf.

**2-** Agregue el parámetro de informe 'IsListSectionSupported' y establezca el valor en True como se muestra en el párrafo 'List Section'.
**3-** Agregue una propiedad personalizada para el elemento de informe que desea que aparezca en la Tabla de Contenidos, Lista de Tablas o Figuras.

{{% /alert %}}

{{% alert color="primary" %}}

**Nombre de Propiedad Personalizada** :IsInList
**Valor de Propiedad** :Boolean
**Valor de Propiedad Personalizada** : True or False

{{% alert color="primary" %}}

Marca el elemento de informe actual como listado por índice en la tabla de contenido, o en la lista de tablas o figuras.

{{% /alert %}}

**Nombre de propiedad personalizada** : Título
**Tipo de propiedad personalizada** : String

{{% alert color="primary" %}}

El título del elemento que se muestra en el índice, lista de tablas o figuras.
{{% /alert %}}

**Nombre de propiedad personalizada** : ListLevel
**Tipo de propiedad personalizada** : Entero

{{% alert color="primary" %}}

El nivel de los elementos listados que se muestra en la tabla de contenidos.

{{% /alert %}}

{{% /alert %}}


