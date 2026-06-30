---
title: Licencias y limitaciones
linktitle: Licencias y limitaciones
type: docs
weight: 50
url: /es/androidjava/licensing/
description: Aspose.PDF for Android via Java invita a sus clientes a obtener una licencia Classic y una licencia Metered. Así como usar una licencia limitada para explorar mejor el producto.
lastmod: "2026-06-30"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Limitación de una versión de evaluación

Queremos que nuestros clientes prueben nuestros componentes a fondo antes de comprar, por lo que la versión de evaluación le permite usarlo como lo haría normalmente.

- **PDF creado con una marca de agua de evaluación.** La versión de evaluación de Aspose.PDF para Android a través de Java ofrece la funcionalidad completa del producto, pero todas las páginas de los documentos PDF generados llevan una marca de agua con "Evaluation Only. Created with Aspose.PDF. Copyright 2002-2020 Aspose Pty Ltd" en la parte superior.

- **El límite del número de elementos de la colección que se pueden procesar.**
En la versión de evaluación de cualquier colección, solo puedes procesar cuatro elementos (por ejemplo, solo 4 páginas, 4 campos de formulario, etc.).

Puedes descargar una versión de evaluación de Aspose.PDF para Android a través de Java desde [Repositorio Aspose](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-pdf). La versión de evaluación proporciona absolutamente las mismas capacidades que la versión licenciada del producto. Además, la versión de evaluación simplemente se vuelve licenciada cuando adquiere una licencia y agrega un par de líneas de código para aplicar la licencia.

Una vez que esté satisfecho con su evaluación de **Aspose.PDF**, puede [adquirir una licencia](https://purchase.aspose.com/) en el sitio web de Aspose. Familiarícese con los diferentes tipos de suscripción que se ofrecen. Si tiene alguna pregunta, no dude en contactar al equipo de ventas de Aspose.

Cada licencia de Aspose incluye una suscripción de un año para actualizaciones gratuitas a cualquier versión nueva o correcciones que se publiquen durante ese tiempo. El soporte técnico es gratuito e ilimitado y se brinda tanto a usuarios con licencia como a usuarios de evaluación.

>Si desea probar Aspose.PDF para Android mediante Java sin las limitaciones de la versión de evaluación, también puede solicitar una Licencia Temporal de 30 días. Por favor, consulte [¿Cómo obtener una Licencia Temporal?](https://purchase.aspose.com/temporary-license)

## Licencia clásica

La licencia se puede cargar desde un archivo u objeto de flujo. La forma más sencilla de establecer una licencia es colocar el archivo de licencia en la misma carpeta que el archivo Aspose.PDF.dll y especificar el nombre del archivo sin una ruta, como se muestra en el ejemplo a continuación.

La licencia es un archivo XML de texto plano que contiene detalles como el nombre del producto, el número de desarrolladores a los que está licenciada, la fecha de vencimiento de la suscripción, etc. El archivo está firmado digitalmente, por lo que no lo modifique; incluso la incorporación inadvertida de una línea adicional en el archivo lo invalidará.

Debe establecer una licencia antes de realizar cualquier operación con documentos. Solo se requiere establecer la licencia una vez por aplicación o proceso.

La licencia puede cargarse desde un flujo o archivo en las siguientes ubicaciones:

1. Ruta explícita.
1. La carpeta que contiene el aspose-pdf-xx.x.jar.

Utilice el método License.setLicense para licenciar el componente. A menudo, la forma más fácil de establecer una licencia es colocar el archivo de licencia en la misma carpeta que Aspose.PDF.jar y especificar solo el nombre del archivo sin ruta, como se muestra en el siguiente ejemplo:

{{% alert color="primary" %}}

A partir de Aspose.PDF for Java 4.2.0, debe llamar a las siguientes líneas de código para inicializar la licencia.

{{% /alert %}}

### Cargando una licencia desde un archivo

En este ejemplo **Aspose.PDF** intentará encontrar el archivo de licencia en la carpeta que contiene los JARs de su aplicación.

```java
// Initialize License Instance
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Call setLicense method to set license
license.setLicense("Aspose.Pdf.Java.lic");
```

### Cargando la licencia desde un objeto de flujo

El siguiente ejemplo muestra cómo cargar una licencia desde un flujo.

```java
// Initialize License Instance
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Set license from Stream
license.setLicense(new java.io.FileInputStream("Aspose.Pdf.Java.lic"));
```

#### Configurando una licencia adquirida antes del 2005/01/22

**Aspose.PDF** para Java ya no admite licencias antiguas, así que por favor contacte a nuestro [equipo de ventas](https://company.aspose.com/contact) para obtener un nuevo archivo de licencia.

### Validar la licencia

Es posible validar si la licencia se ha configurado correctamente o no. La clase Document tiene el método isLicensed que devolverá true si la licencia se ha configurado adecuadamente.

```java
License license = new License();
license.setLicense("Aspose.Pdf.Java.lic");
// Check if license has been validated
if (com.aspose.pdf.Document.isLicensed()) {
    System.out.println("License is Set!");
}
```
## Licencia medida

Aspose.PDF permite a los desarrolladores aplicar una clave medida. Es un nuevo mecanismo de licenciamiento. El nuevo mecanismo de licenciamiento se utilizará junto con el método de licenciamiento existente. Los clientes que deseen ser facturados según el uso de las funciones de la API pueden utilizar el licenciamiento medido. Para obtener más detalles, consulte [FAQ de licenciamiento medido](https://purchase.aspose.com/faqs/licensing/metered) sección.

```java
String publicKey = "";
String privateKey = "";

Metered m = new Metered();
m.setMeteredKey(publicKey, privateKey);

// Optionally, the following two lines returns true if a valid license has been applied;
// false if the component is running in evaluation mode.
License lic = new License();
System.out.println("License is set = " + lic.isLicensed());
```
## Uso de varios productos de Aspose

Si utilizas varios productos de Aspose en tu aplicación, por ejemplo Aspose.PDF y Aspose.Words, aquí tienes algunos consejos útiles.

- **Establece la licencia para cada producto de Aspose por separado.** Incluso si tienes un solo archivo de licencia para todos los componentes, por ejemplo ‘Aspose.Total.lic’, aún necesitas llamar a **License.SetLicense** por separado para cada producto de Aspose que estés usando en tu aplicación.
- **Utiliza el nombre completo de la clase de licencia.** Cada producto de Aspose tiene una clase **License** en su espacio de nombres. Por ejemplo, Aspose.PDF tiene la clase **com.aspose.pdf.License** y Aspose.Words tiene la clase **com.aspose.words.License**. Utilizar el nombre de clase totalmente calificado te permite evitar cualquier confusión sobre qué licencia se aplica a qué producto.

```java
// Instantiate the License class of Aspose.Pdf
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Set the license
license.setLicense("Aspose.Total.Java.lic");

// Setting license for Aspose.Words for Java

// Instantiate the License class of Aspose.Words
com.aspose.words.License licenseaw = new com.aspose.words.License();
// Set the license
licenseaw.setLicense("Aspose.Total.Java.lic");
```
