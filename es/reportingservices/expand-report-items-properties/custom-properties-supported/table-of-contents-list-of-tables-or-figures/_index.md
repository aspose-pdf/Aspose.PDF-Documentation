---
title: Tabla de Contenidos Lista de Tablas o Figuras
type: docs
weight: 10
url: es/reportingservices/table-of-contents-list-of-tables-or-figures/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

El Diseñador de Informes no admite la adición de tabla de contenidos para documentos de informes. Con Aspose.Pdf para Reporting Services, puede instruir fácilmente al renderizador de PDF para producir documentos PDF con Tabla de Contenidos, o Lista de Tablas o Figuras. Puede hacerlo en los siguientes pasos:

{{% /alert %}}

{{% alert color="primary" %}}
Asegúrese de que el archivo Aspose.Pdf.ListSectionStyle.xml exista en ```<Instance>```/bin, donde ```<Instance>``` es el directorio del Servidor de Informes. Si el archivo no existe, créelo en el directorio ```<Instance>```/bin y coloque el siguiente marcado dentro.

## Tabla de Contenidos

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

## Lista de Tablas

**Ejemplo**

```cs
<ListSection ListType="ListOfTables">
              <Title>
            <Segment IsTrueTypeFontBold="true" FontSize="30">ListOfTables</Segment>
              </Title>
</ListSection>
```

## Lista de Figuras

**Ejemplo**

```cs
 <ListSection ListType="ListOfFigures">
    <Title>
            <Segment IsTrueTypeFontBold="true" FontSize="30">ListOfFigures</Segment>
    </Title>
</ListSection>

```

Por favor, consulte la sección 'Trabajando con TOC' de la documentación en línea de Aspose.Pdf.

**2-** Agregue el parámetro de informe 'IsListSectionSupported' y establezca el valor en True como se muestra en el párrafo 'Sección de Lista'.
**3-** Agregue una propiedad personalizada para su elemento de informe que desee que esté listado en la Tabla de Contenidos, Lista de Tablas o Figuras.

{{% /alert %}}

{{% alert color="primary" %}}

**Nombre de la Propiedad Personalizada** :IsInList
**Valor de la Propiedad** :Boolean
**Valor de la Propiedad Personalizada** : True o False

{{% alert color="primary" %}}

Marca el elemento de informe actual como listado por índice en la tabla de contenidos, o la lista de tablas o figuras.

{{% /alert %}}

**Custom Property Name** : Title
**Custom Property Type** : String

{{% alert color="primary" %}}

El título del ítem mostrado en la tabla de contenido, lista de tablas o figuras.
{{% /alert %}}

**Custom Property Name** : ListLevel
**Custom Property Type** : Integer

{{% alert color="primary" %}}

El nivel de los ítems listados mostrados en la tabla de contenido.

{{% /alert %}}

{{% /alert %}}