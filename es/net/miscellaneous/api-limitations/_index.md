---
title: Limitaciones de la API
type: docs
weight: 70
url: es/net/api-limitations/
---

## **Xsl Fo a Pdf**
A continuación se presentan los problemas conocidos del soporte de XSL-FO.

- SVG no es compatible
## **Información del creador de PDF**
- Tenga en cuenta que no puede establecer valores en los campos **Application** y **Producer**, porque se mostrarán Aspose Ltd. y Aspose.PDF para .NET x.x.x en estos campos
## **Otros**
A continuación se presentan algunos otros problemas conocidos.

- Pdf/X no es compatible.
- El formulario XFA dinámico no es compatible: ya que sus páginas se crean/renderizan en el momento de la carga del PDF, en Adobe Acrobat/Reader. Por lo tanto, no podemos extraer y guardar ninguna de estas páginas virtuales o varias páginas. En su lugar, nosotros (y Adobe Acrobat) solo podemos extraer una verdadera página que contiene solo un mensaje de error.
- Los símbolos especiales $p y $P no funcionarán si no terminan con un carácter en blanco.
- Conversión de HTML a PDF: HTML es un lenguaje muy extenso y con cada nueva versión de Aspose.PDF para .NET, hacemos nuestro mejor esfuerzo para ofrecer una versión más sólida y mejorada de la conversión de HTML a PDF (*apoyando todo tipo de HTML*) pero como hay numerosos archivos HTML con diferente naturaleza/estructura y complejidad, a veces nuestro componente encuentra algunos problemas en términos de formato al renderizar contenidos HTML al formato PDF y generalmente ocurre cuando se usan documentos con estructura compleja.
- Conversión de HTML a PDF: HTML es un lenguaje muy extenso y con cada nueva versión de Aspose.PDF para .NET, hacemos nuestro mejor esfuerzo para entregar una versión mejor y más robusta de la conversión de HTML a PDF (*apoyando todo tipo de HTML*), pero como hay numerosos archivos HTML con diferentes naturalezas/estructuras y complejidades, a veces nuestro componente encuentra algunos problemas en términos de formateo al renderizar contenidos HTML en formato PDF y esto generalmente ocurre cuando se utilizan documentos con estructuras complejas.
- La incrustación de fuentes no es compatible en MS Word para Macintosh y también tenga en cuenta que en MS Word para Windows, solo se limita a fuentes TrueType. Por lo tanto, al visualizar archivos word (DOC) generados como resultado de la conversión de PDF a DOC a través de Aspose.PDF para .NET, las fuentes incrustadas son sustituidas al ver los archivos en MS Word en MAC OS. Para más detalles, por favor eche un vistazo a [macsupportcentral](http://www.macsupportcentral.com/2012/05/embed-fonts-microsoft-office-word-files/).
