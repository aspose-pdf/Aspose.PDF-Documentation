---
title: Obtener Valor de Opción de Botón
type: docs
weight: 40
url: /net/get-button-option-value/
description: Esta sección explica cómo obtener el Valor de Opción de Botón con Aspose.PDF Facades usando la Clase Form.
lastmod: "2021-06-05"
draft: false
---

## Obtener Valores de Opción de Botón de un Archivo PDF Existente

Los botones de radio proporcionan una forma de mostrar diferentes opciones. La clase [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) te permite obtener todos los valores de opción de botón para un botón de radio en particular. Puedes obtener estos valores usando el método [GetButtonOptionValues](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/getbuttonoptionvalues). Este método requiere el nombre del botón de radio como parámetro de entrada y devuelve un Hashtable. Puedes iterar a través de este Hashtable para obtener los valores de opción. El siguiente fragmento de código te muestra cómo obtener valores de opción de botón de un archivo PDF existente.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Forms-GetButtonOptionValue-GetButtonOptionValue.cs" >}}

## Obtener el Valor de Opción Actual del Botón de un Archivo PDF Existente

Los botones de opción proporcionan una forma de establecer valores de opción, sin embargo, solo uno de ellos puede ser seleccionado a la vez. Si deseas obtener el valor de opción actualmente seleccionado, puedes usar el método [GetButtonOptionCurrentValue**. La clase [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) proporciona este método. El método [GetButtonOptionCurrentValue](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/getbuttonoptioncurrentvalue) requiere el nombre del botón de opción como parámetro de entrada y devuelve el valor como cadena. El siguiente fragmento de código te muestra cómo obtener el valor de la opción actual del botón de un archivo PDF existente.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Forms-GetButtonOptionValue-GetCurrentValue.cs" >}}