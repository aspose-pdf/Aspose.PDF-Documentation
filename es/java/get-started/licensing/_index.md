---
title: Licensing and limitations
linktitle: Licensing and limitations
type: docs
weight: 90
url: es/java/licensing/
description: Aspose. PDF for Java invita a sus clientes a obtener una licencia Clásica y una Licencia Medida. Así como usar una licencia limitada para explorar mejor el producto.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Limitación de una versión de evaluación

Queremos que nuestros clientes prueben a fondo nuestros componentes antes de comprar, por lo que la versión de evaluación le permite usarlo como lo haría normalmente.

- **PDF creado con una marca de agua de evaluación.** La versión de evaluación de Aspose.PDF para Java proporciona toda la funcionalidad del producto, pero todas las páginas en los documentos PDF generados están marcadas con "Solo Evaluación. Creado con Aspose.PDF. Copyright 2002-2020 Aspose Pty Ltd" en la parte superior.

- **El límite del número de elementos de colección que se pueden procesar.**

En la versión de evaluación de cualquier colección, solo puede procesar cuatro elementos (por ejemplo, solo 4 páginas, 4 campos de formulario, etc.).

You can download an evaluation version of **Aspose.PDF** para Java desde [Aspose Repository](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-pdf). La versión de evaluación ofrece exactamente las mismas capacidades que la versión con licencia del producto. Además, la versión de evaluación simplemente se convierte en licenciada cuando compras una licencia y añades un par de líneas de código para aplicar la licencia.

Una vez que estés satisfecho con tu evaluación de **Aspose.PDF**, puedes [comprar una licencia](https://purchase.aspose.com/) en el sitio web de Aspose. Familiarízate con los diferentes tipos de suscripción ofrecidos. Si tienes alguna pregunta, no dudes en contactar al equipo de ventas de Aspose.

Cada licencia de Aspose incluye una suscripción de un año para actualizaciones gratuitas a cualquier nueva versión o corrección que se publique durante este tiempo. El soporte técnico es gratuito e ilimitado y se proporciona tanto a usuarios con licencia como de evaluación.

>Si deseas probar Aspose.PDF para Java sin las limitaciones de la versión de evaluación, también puedes solicitar una Licencia Temporal de 30 días.
 Por favor, consulte [Cómo obtener una licencia temporal?](https://purchase.aspose.com/temporary-license)

## Licencia clásica

La licencia se puede cargar desde un archivo o un objeto de flujo. La forma más fácil de establecer una licencia es colocar el archivo de licencia en la misma carpeta que el archivo Aspose.PDF.dll y especificar el nombre del archivo sin una ruta, como se muestra en el ejemplo a continuación.

La licencia es un archivo XML de texto plano que contiene detalles como el nombre del producto, el número de desarrolladores a los que está licenciada, la fecha de expiración de la suscripción, etc. El archivo está firmado digitalmente, por lo que no modifique el archivo; incluso la adición inadvertida de un salto de línea adicional en el archivo lo invalidará.

Necesita establecer una licencia antes de realizar cualquier operación con documentos. Solo se requiere establecer una licencia una vez por aplicación o proceso.

La licencia se puede cargar desde un flujo o archivo en las siguientes ubicaciones:

1. Ruta explícita.
1. La carpeta que contiene el archivo aspose-pdf-xx.x.jar.

Utilice el método License.setLicense para licenciar el componente. A menudo, la forma más fácil de establecer una licencia es colocar el archivo de licencia en la misma carpeta que Aspose.PDF.jar y especificar solo el nombre del archivo sin la ruta, como se muestra en el siguiente ejemplo:

{{% alert color="primary" %}}

A partir de Aspose.PDF para Java 4.2.0, necesitas llamar a las siguientes líneas de código para inicializar la licencia.

{{% /alert %}}

### Cargando una licencia desde un archivo

En este ejemplo, **Aspose.PDF** intentará encontrar el archivo de licencia en la carpeta que contiene los JARs de tu aplicación.

```java
// Inicializar instancia de licencia
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Llamar al método setLicense para establecer la licencia
license.setLicense("Aspose.Pdf.Java.lic");
```
### Cargando la licencia desde un objeto de flujo

El siguiente ejemplo muestra cómo cargar una licencia desde un flujo.

```java
// Inicializar instancia de licencia
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Establecer la licencia desde un flujo
license.setLicense(new java.io.FileInputStream("Aspose.Pdf.Java.lic"));
```

#### Estableciendo una Licencia Comprada Antes del 22/01/2005**Aspose.PDF** para Java ya no admite licencias antiguas, así que por favor contacte a nuestro [equipo de ventas](https://company.aspose.com/contact) para obtener un nuevo archivo de licencia.

### Validar la Licencia

Es posible validar si la licencia se ha establecido correctamente o no. La clase Document tiene el método isLicensed que devolverá true si la licencia se ha establecido correctamente.

```java
License license = new License();
license.setLicense("Aspose.Pdf.Java.lic");
// Verificar si la licencia ha sido validada
if (com.aspose.pdf.Document.isLicensed()) {
    System.out.println("¡Licencia Establecida!");
}
```
## Licencia Medida

Aspose.PDF permite a los desarrolladores aplicar una clave medida. Es un nuevo mecanismo de licenciamiento. El nuevo mecanismo de licenciamiento se utilizará junto con el método de licenciamiento existente. Aquellos clientes que deseen ser facturados en función del uso de las características de la API pueden usar la licencia medida. Para más detalles, por favor consulte la sección [Preguntas Frecuentes sobre Licencias Medidas](https://purchase.aspose.com/faqs/licensing/metered).

Se ha introducido una nueva clase [Metered](https://reference.aspose.com/pdf/java/com.aspose.pdf/Metered) para aplicar la clave medida.
 A continuación se muestra el código de muestra que demuestra cómo establecer la clave pública y privada medida.

```java
String publicKey = "";
String privateKey = "";

Metered m = new Metered();
m.setMeteredKey(publicKey, privateKey);

// Opcionalmente, las siguientes dos líneas devuelven verdadero si se ha aplicado una licencia válida;
// falso si el componente está ejecutándose en modo de evaluación.
License lic = new License();
System.out.println("La licencia está establecida = " + lic.isLicensed());
```
## Uso de Múltiples Productos de Aspose

Si utiliza múltiples productos de Aspose en su aplicación, por ejemplo Aspose.PDF y Aspose.Words, aquí hay algunos consejos útiles.

- **Establezca la Licencia para cada Producto Aspose por Separado.** Incluso si tiene un único archivo de licencia para todos los componentes, por ejemplo 'Aspose.Total.lic', todavía necesita llamar a **License.SetLicense** por separado para cada producto Aspose que está utilizando en su aplicación.
- **Use el Nombre de Clase de Licencia Totalmente Calificado.** Cada producto Aspose tiene una clase **License** en su espacio de nombres. Por ejemplo, Aspose.PDF tiene la clase **com.aspose.pdf.License** y Aspose.Words tiene la clase **com.aspose.words.License**. Usar el nombre de clase totalmente calificado te permite evitar cualquier confusión sobre qué licencia se aplica a qué producto.

```java
// Instanciar la clase License de Aspose.Pdf
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Establecer la licencia
license.setLicense("Aspose.Total.Java.lic");

// Estableciendo licencia para Aspose.Words para Java

// Instanciar la clase License de Aspose.Words
com.aspose.words.License licenseaw = new com.aspose.words.License();
// Establecer la licencia
licenseaw.setLicense("Aspose.Total.Java.lic");
```