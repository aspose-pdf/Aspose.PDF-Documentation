---
title: Licencia Aspose PDF
linktitle: Licencias y limitaciones
type: docs
weight: 50
url: /java/licensing/
description: Aspose.PDF para Python invita a sus clientes a obtener una licencia clásica. Además de utilizar una licencia limitada para explorar mejor el producto.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Licencia de Aspose.PDF para Java
Abstract: El artículo analiza las limitaciones y opciones de licencia de Aspose.PDF para Python. Destaca que la versión de evaluación permite probar la funcionalidad completa, pero agrega una marca de agua a los archivos PDF generados, que indica "Sólo evaluación" junto con la información de derechos de autor. Para los usuarios que deseen realizar pruebas sin estas limitaciones, hay disponible una licencia temporal de 30 días. El artículo explica con más detalle cómo implementar una licencia clásica cargándola desde un archivo o flujo, recomendando colocar el archivo de licencia en el mismo directorio que el archivo Aspose.PDF.dll y configurar la licencia usando la clase `Aspose.Pdf.License`. Se proporcionan fragmentos de código para ilustrar el proceso de concesión de licencias.
---
## Limitación de una versión de evaluación



Queremos que nuestros clientes prueben minuciosamente nuestros componentes antes de comprarlos para que la versión de evaluación le permita usarlos como lo haría normalmente.


- **PDF creado con una marca de agua de evaluación.** La versión de evaluación de Aspose.PDF para Java proporciona funcionalidad completa del producto, pero todas las páginas de los documentos PDF generados tienen una marca de agua con "Solo evaluación. Creado con Aspose.PDF. Copyright 2002-2020 Aspose Pty Ltd" en la parte superior.


- **El límite de la cantidad de artículos de colección que se pueden procesar.**


En la versión de evaluación de cualquier colección, solo puedes procesar cuatro elementos (por ejemplo, solo 4 páginas, 4 campos de formulario, etc.).

Puede descargar una versión de evaluación de **Aspose.PDF** para Java desde [Aspose Repository](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-pdf). La versión de evaluación proporciona absolutamente las mismas capacidades que la versión con licencia del producto. Además, la versión de evaluación simplemente adquiere la licencia cuando usted compra una licencia y agrega un par de líneas de código para aplicar la licencia.



Una vez que esté satisfecho con su evaluación de **Aspose.PDF**, puede [comprar una licencia](https://purchase.aspose.com/) en el sitio web de Aspose. Familiarícese con los diferentes tipos de suscripción que se ofrecen. Si tienes alguna pregunta, no dudes en contactar con el equipo comercial de Aspose.



Cada licencia de Aspose incluye una suscripción de un año para actualizaciones gratuitas de cualquier nueva versión o corrección que surja durante este tiempo. El soporte técnico es gratuito e ilimitado y se proporciona tanto a usuarios con licencia como a usuarios de evaluación.



>Si desea probar Aspose.PDF para Java sin las limitaciones de la versión de evaluación, también puede solicitar una licencia temporal de 30 días. Consulte [¿Cómo obtener una licencia temporal?](https://purchase.aspose.com/temporary-license)


## 
Licencia clásica

La licencia se puede cargar desde un archivo u objeto de flujo. La forma más sencilla de configurar una licencia es colocar el archivo de licencia en la misma carpeta que el archivo Aspose.PDF.dll y especificar el nombre del archivo sin una ruta, como se muestra en el siguiente ejemplo.



La licencia es un archivo XML de texto sin formato que contiene detalles como el nombre del producto, la cantidad de desarrolladores para los que tiene licencia, la fecha de vencimiento de la suscripción, etc. El archivo está firmado digitalmente, así que no lo modifique; incluso la adición inadvertida de un salto de línea adicional al archivo lo invalidará.



Debe configurar una licencia antes de realizar cualquier operación con documentos. Solo es necesario establecer una licencia una vez por solicitud o proceso.



La licencia se puede cargar desde una secuencia o archivo en las siguientes ubicaciones:


1. Camino explícito.
1. La carpeta que contiene el archivo aspose-pdf-xx.x.jar.



Utilice el método License.setLicense para obtener la licencia del componente. A menudo, la forma más sencilla de configurar una licencia es colocar el archivo de licencia en la misma carpeta que Aspose.PDF.jar y especificar solo el nombre del archivo sin la ruta, como se muestra en el siguiente ejemplo:


{{% alert color="primary" %}}


A partir de Aspose.PDF para Java 4.2.0, debe llamar a las siguientes líneas de código para inicializar la licencia.


{{% /alert %}}

### 
Cargando una licencia desde un archivo



En este ejemplo, **Aspose.PDF** intentará encontrar el archivo de licencia en la carpeta que contiene los archivos JAR de su aplicación.

```java
// Initialize License Instance
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Call setLicense method to set license
license.setLicense("Aspose.Pdf.Java.lic");
```

### Cargando la licencia desde un objeto de flujo



El siguiente ejemplo muestra cómo cargar una licencia desde una secuencia.


```java
// Initialize License Instance
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Set license from Stream
license.setLicense(new java.io.FileInputStream("Aspose.Pdf.Java.lic"));
```

### 
Validar la licencia



Es posible validar si la licencia se ha configurado correctamente o no. La clase Documento tiene el método isLicensed que devolverá verdadero si la licencia se ha configurado correctamente.


```java
License license = new License();
license.setLicense("Aspose.Pdf.Java.lic");
// Check if license has been validated
if (com.aspose.pdf.Document.isLicensed()) {
    System.out.println("License is Set!");
}
```

## 
Licencia medida

Aspose.PDF permite a los desarrolladores aplicar claves medidas. Es un nuevo mecanismo de concesión de licencias. El nuevo mecanismo de concesión de licencias se utilizará junto con el método de concesión de licencias existente. Aquellos clientes que deseen que se les facture en función del uso de las funciones API pueden utilizar la licencia medida. Para obtener más detalles, consulte la sección [Preguntas frecuentes sobre licencias medidas](https://purchase.aspose.com/faqs/licensing/metered).



Se ha introducido una nueva clase [medida](https://reference.aspose.com/pdf/java/com.aspose.pdf/Metered) para aplicar la clave medida. A continuación se muestra el código de muestra que demuestra cómo configurar la clave pública y privada medida.


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

## 
Uso de varios productos de Aspose



Si utiliza varios productos Aspose en su aplicación, por ejemplo Aspose.PDF y Aspose.Words, aquí le ofrecemos algunos consejos útiles.


- **Establezca la licencia para cada producto Aspose por separado.** Incluso si tiene un único archivo de licencia para todos los componentes, por ejemplo 'Aspose.Total.lic', aún necesita llamar a **License.SetLicense** por separado para cada producto Aspose que esté utilizando en su aplicación.
- **Utilice un nombre de clase de licencia totalmente calificado.** Cada producto Aspose tiene una clase **Licencia** en su espacio de nombres. Por ejemplo, Aspose.PDF tiene la clase **com.aspose.pdf.License** y Aspose.Words tiene la clase **com.aspose.words.License**. El uso del nombre de clase completo le permite evitar cualquier confusión sobre qué licencia se aplica a qué producto.

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
