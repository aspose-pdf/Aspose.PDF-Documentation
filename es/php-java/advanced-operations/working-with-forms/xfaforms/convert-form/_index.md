---
title: Convertir formulario XFA a AcroForm
linktitle: Convertir formulario XFA
type: docs
weight: 10
url: /es/php-java/convert-form/
description: Esta sección explica cómo convertir un formulario XFA a AcroForm con Aspose.PDF para PHP a través de Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Convertir formulario XFA dinámico a AcroForm estándar

Los formularios dinámicos se basan en una especificación XML conocida como XFA, la "Arquitectura de Formularios XML". También se puede convertir un formulario XFA dinámico a un Acroform estándar. La información sobre el formulario (en lo que respecta al PDF) es muy vaga: especifica que existen campos, con propiedades y eventos JavaScript, pero no especifica ningún renderizado. Los objetos del formulario XFA se dibujan en el momento de cargar el documento.

Actualmente, PDF admite dos métodos diferentes para integrar datos y formularios PDF:

- AcroForms (también conocidos como formularios Acrobat), introducidos e incluidos en la especificación del formato PDF 1.2.

- Adobe XML Forms Architecture (XFA) forms, introducidas en la especificación del formato PDF 1.5 como una característica opcional. (La especificación de XFA no está incluida en la especificación PDF, solo se hace referencia a ella.)

No es posible extraer o manipular páginas de Formularios XFA, porque el contenido del formulario se genera en tiempo de ejecución (durante la visualización del formulario XFA) dentro de la aplicación que intenta mostrar o renderizar el formulario XFA. Aspose.PDF tiene una característica que permite a los desarrolladores convertir formularios XFA a AcroForms estándar.

```php

        // Cargar formulario XFA
        $document = new Document($inputFile);
        
        // Establecer el tipo de campos del formulario como AcroForm estándar
        $formType = new FormType();
        $document->getForm()->setType($formType->getStandard());
            
        // Guardar el documento actualizado
        $document->save($outputFile);
        
        // Guardar PDF modificado    
        $document->close();
```