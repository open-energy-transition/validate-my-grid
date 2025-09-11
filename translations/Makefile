PO:=$(wildcard *.po)
LANG_=en.lang $(PO:.po=.lang)

all: ../power.validator.zip

../voltages.validator.mapcss: ../data/voltages.csv
	python3 ../scripts/generate_country_specific_rules.py >> $@

power_mapcss.pot: ../power.validator.mapcss ../voltages.validator.mapcss
	sed -i "s/^#: .*//" $@
	xgettext --join-existing -cTRANSLATORS \
	  --keyword=tr \
	  --language=C \
	  --force-po --omit-header \
	  --output=$@ ../*.validator.mapcss

%.po: power_mapcss.pot
	msgmerge --no-fuzzy-matching --update $@ $<

i18n.pl:
	wget https://raw.githubusercontent.com/openstreetmap/svn-archive/main/applications/editors/josm/i18n/i18n.pl

en.lang: $(PO) i18n.pl
	perl i18n.pl --potfile=power_mapcss.pot $(patsubst %,./%,$(PO))

../power.validator.zip: ../power.validator.mapcss ../voltages.validator.mapcss en.lang
	rm -f $@
	mkdir -p data
	perl i18n.pl --potfile=power_mapcss.pot ./fr.po
	mv $(LANG_) data
	zip $@ data/*
	cat ../power.validator.mapcss ../voltages.validator.mapcss >> ../powerQA.validator.mapcss
	zip -j $@ ../powerQA.validator.mapcss
	zip -j $@ ../MapYourGrid-favicon.png
	rm -fr data
	rm -f ../powerQA.validator.mapcss

clean:
	rm -f $(LANG_)
	rm -fr data
	rm -f i18n.pl
	rm -f ../power.validator.zip
	rm -f ../voltages.validator.mapcss
	rm *.po~
