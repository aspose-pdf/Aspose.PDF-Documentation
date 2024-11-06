---
title: Explorando características de la clase FormEditor
type: docs
weight: 10
url: es/net/exploring-features-of-formeditor-class/
description: Puedes aprender detalles sobre la exploración de características de la clase FormEditor con Aspose. PDF para la biblioteca .NET
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

Los documentos PDF a veces contienen formularios interactivos, que se conocen como AcroForm. Es como un formulario utilizado en las páginas web. Estos formularios contienen diferentes tipos de controles, es decir, cuadros de texto, casillas de verificación y botones, etc. Un desarrollador que trabaja con archivos PDF a veces puede tener que editar estos formularios. En este artículo, analizaremos en detalle cómo el [espacio de nombres Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) nos permite hacer eso.

{{% /alert %}}

## Detalles de implementación

Los desarrolladores pueden usar el [espacio de nombres Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) no solo para agregar nuevos formularios y campos de formulario en un documento PDF, sino que también les permite editar campos existentes. El alcance de este artículo se limita a las características de [Aspose.PDF para .NET](/pdf/net/) que tratan con la edición de formularios.

[FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) es la clase que contiene la mayoría de los métodos y propiedades que permiten a los desarrolladores editar campos de formulario. No solo se pueden agregar nuevos campos, sino también eliminar campos existentes, mover un campo a otra posición, cambiar el nombre del campo o atributos, etc. La lista de características proporcionadas por esta clase es bastante completa, y es muy fácil trabajar con los campos de formulario usando esta clase.

Estos métodos se pueden dividir en dos categorías principales, una de las cuales se utiliza para manipular los campos, y la otra se utiliza para establecer los nuevos atributos de estos campos. Los métodos que podemos agrupar bajo la primera categoría incluyen AddField, AddListItem, RemoveListItem, CopyInnerField, CopyOuterField, DelListItem, MoveField, RemoveField, y RenameField, etc. En la segunda categoría de los métodos se pueden incluir SetFieldAlignment, SetFieldAppearance, SetFieldAttribute, SetFieldLimit, SetFieldScript. El siguiente fragmento de código te muestra algunos de los métodos de la clase FormEditor en funcionamiento:



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-FormEditorFeatures-FormEditorFeatures.cs" >}}