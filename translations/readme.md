# How do translations work ?

## When you want to add a new rule

* Create new rules in `power.validator.mapcss`
* Then, inside the `translations` directory, run `make *.po`. It will update the `.pot` file.
* Commit `power.validator.mapcss` & the `.pot` file. The build system will make your new rules available to the JOSM community

## When you want to translate some rules in your langage

* Update the `*.po` file
* To test your changes in JOSM, rum `make` from the `translations` directory. It will generate a zip file that you can reference in JOSM preferences
* When you are ready to chommit your changes, run `make clean` from the `translations` directory.
* Commit the `*.po` file. The build system will make the zip and make it available to the JOSM community