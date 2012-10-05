# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'AttributionDePupitre.author'
        db.add_column('catalogue_attributiondepupitre', 'author',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'ParenteDIndividus.author'
        db.add_column('catalogue_parentedindividus', 'author',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'TypeDeSource.author'
        db.add_column('catalogue_typedesource', 'author',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Engagement.author'
        db.add_column('catalogue_engagement', 'author',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'TypeDePersonnel.author'
        db.add_column('catalogue_typedepersonnel', 'author',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Profession.author'
        db.add_column('catalogue_profession', 'author',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Saison.author'
        db.add_column('catalogue_saison', 'author',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'CaracteristiqueDOeuvre.author'
        db.add_column('catalogue_caracteristiquedoeuvre', 'author',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Illustration.author'
        db.add_column('catalogue_illustration', 'author',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'NatureDeLieu.author'
        db.add_column('catalogue_naturedelieu', 'author',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Source.author'
        db.add_column('catalogue_source', 'author',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Pupitre.author'
        db.add_column('catalogue_pupitre', 'author',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'GenreDOeuvre.author'
        db.add_column('catalogue_genredoeuvre', 'author',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'TypeDeParenteDOeuvres.author'
        db.add_column('catalogue_typedeparentedoeuvres', 'author',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Partie.author'
        db.add_column('catalogue_partie', 'author',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Prenom.author'
        db.add_column('catalogue_prenom', 'author',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Devise.author'
        db.add_column('catalogue_devise', 'author',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Auteur.author'
        db.add_column('catalogue_auteur', 'author',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Personnel.author'
        db.add_column('catalogue_personnel', 'author',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'CaracteristiqueDElementDeProgramme.author'
        db.add_column('catalogue_caracteristiquedelementdeprogramme', 'author',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Individu.author'
        db.add_column('catalogue_individu', 'author',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Document.author'
        db.add_column('catalogue_document', 'author',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Oeuvre.author'
        db.add_column('catalogue_oeuvre', 'author',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Lieu.author'
        db.add_column('catalogue_lieu', 'author',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'ElementDeProgramme.author'
        db.add_column('catalogue_elementdeprogramme', 'author',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'TypeDeParenteDIndividus.author'
        db.add_column('catalogue_typedeparentedindividus', 'author',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Etat.author'
        db.add_column('catalogue_etat', 'author',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Evenement.author'
        db.add_column('catalogue_evenement', 'author',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'TypeDeCaracteristiqueDOeuvre.author'
        db.add_column('catalogue_typedecaracteristiquedoeuvre', 'author',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'AncrageSpatioTemporel.author'
        db.add_column('catalogue_ancragespatiotemporel', 'author',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'ParenteDOeuvres.author'
        db.add_column('catalogue_parentedoeuvres', 'author',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'AttributionDePupitre.author'
        db.delete_column('catalogue_attributiondepupitre', 'author_id')

        # Deleting field 'ParenteDIndividus.author'
        db.delete_column('catalogue_parentedindividus', 'author_id')

        # Deleting field 'TypeDeSource.author'
        db.delete_column('catalogue_typedesource', 'author_id')

        # Deleting field 'Engagement.author'
        db.delete_column('catalogue_engagement', 'author_id')

        # Deleting field 'TypeDePersonnel.author'
        db.delete_column('catalogue_typedepersonnel', 'author_id')

        # Deleting field 'Profession.author'
        db.delete_column('catalogue_profession', 'author_id')

        # Deleting field 'Saison.author'
        db.delete_column('catalogue_saison', 'author_id')

        # Deleting field 'CaracteristiqueDOeuvre.author'
        db.delete_column('catalogue_caracteristiquedoeuvre', 'author_id')

        # Deleting field 'Illustration.author'
        db.delete_column('catalogue_illustration', 'author_id')

        # Deleting field 'NatureDeLieu.author'
        db.delete_column('catalogue_naturedelieu', 'author_id')

        # Deleting field 'Source.author'
        db.delete_column('catalogue_source', 'author_id')

        # Deleting field 'Pupitre.author'
        db.delete_column('catalogue_pupitre', 'author_id')

        # Deleting field 'GenreDOeuvre.author'
        db.delete_column('catalogue_genredoeuvre', 'author_id')

        # Deleting field 'TypeDeParenteDOeuvres.author'
        db.delete_column('catalogue_typedeparentedoeuvres', 'author_id')

        # Deleting field 'Partie.author'
        db.delete_column('catalogue_partie', 'author_id')

        # Deleting field 'Prenom.author'
        db.delete_column('catalogue_prenom', 'author_id')

        # Deleting field 'Devise.author'
        db.delete_column('catalogue_devise', 'author_id')

        # Deleting field 'Auteur.author'
        db.delete_column('catalogue_auteur', 'author_id')

        # Deleting field 'Personnel.author'
        db.delete_column('catalogue_personnel', 'author_id')

        # Deleting field 'CaracteristiqueDElementDeProgramme.author'
        db.delete_column('catalogue_caracteristiquedelementdeprogramme', 'author_id')

        # Deleting field 'Individu.author'
        db.delete_column('catalogue_individu', 'author_id')

        # Deleting field 'Document.author'
        db.delete_column('catalogue_document', 'author_id')

        # Deleting field 'Oeuvre.author'
        db.delete_column('catalogue_oeuvre', 'author_id')

        # Deleting field 'Lieu.author'
        db.delete_column('catalogue_lieu', 'author_id')

        # Deleting field 'ElementDeProgramme.author'
        db.delete_column('catalogue_elementdeprogramme', 'author_id')

        # Deleting field 'TypeDeParenteDIndividus.author'
        db.delete_column('catalogue_typedeparentedindividus', 'author_id')

        # Deleting field 'Etat.author'
        db.delete_column('catalogue_etat', 'author_id')

        # Deleting field 'Evenement.author'
        db.delete_column('catalogue_evenement', 'author_id')

        # Deleting field 'TypeDeCaracteristiqueDOeuvre.author'
        db.delete_column('catalogue_typedecaracteristiquedoeuvre', 'author_id')

        # Deleting field 'AncrageSpatioTemporel.author'
        db.delete_column('catalogue_ancragespatiotemporel', 'author_id')

        # Deleting field 'ParenteDOeuvres.author'
        db.delete_column('catalogue_parentedoeuvres', 'author_id')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'catalogue.ancragespatiotemporel': {
            'Meta': {'ordering': "['date', 'heure', 'lieu__parent', 'lieu', 'date_approx', 'heure_approx', 'lieu_approx']", 'object_name': 'AncrageSpatioTemporel'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_approx': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'heure': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'heure_approx': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lieu': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'ancrages'", 'null': 'True', 'to': "orm['catalogue.Lieu']"}),
            'lieu_approx': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        'catalogue.attributiondepupitre': {
            'Meta': {'ordering': "['pupitre']", 'object_name': 'AttributionDePupitre'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'individus': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'attributions_de_pupitre'", 'symmetrical': 'False', 'to': "orm['catalogue.Individu']"}),
            'pupitre': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'attributions_de_pupitre'", 'to': "orm['catalogue.Pupitre']"})
        },
        'catalogue.auteur': {
            'Meta': {'ordering': "['profession']", 'object_name': 'Auteur'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'individus': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'auteurs'", 'symmetrical': 'False', 'to': "orm['catalogue.Individu']"}),
            'profession': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'auteurs'", 'to': "orm['catalogue.Profession']"})
        },
        'catalogue.caracteristiquedelementdeprogramme': {
            'Meta': {'ordering': "['nom']", 'object_name': 'CaracteristiqueDElementDeProgramme'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'classement': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'nom_pluriel': ('django.db.models.fields.CharField', [], {'max_length': '110', 'blank': 'True'})
        },
        'catalogue.caracteristiquedoeuvre': {
            'Meta': {'ordering': "['type', 'classement']", 'object_name': 'CaracteristiqueDOeuvre'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'classement': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'caracteristiques_d_oeuvre'", 'to': "orm['catalogue.TypeDeCaracteristiqueDOeuvre']"}),
            'valeur': ('django.db.models.fields.CharField', [], {'max_length': '400'})
        },
        'catalogue.devise': {
            'Meta': {'object_name': 'Devise'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200', 'blank': 'True'}),
            'symbole': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10'})
        },
        'catalogue.document': {
            'Meta': {'ordering': "['document']", 'object_name': 'Document'},
            'auteurs': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'documents'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['catalogue.Auteur']"}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'description': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'document': ('filebrowser.fields.FileBrowseField', [], {'max_length': '400'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'})
        },
        'catalogue.elementdeprogramme': {
            'Meta': {'ordering': "['classement', 'oeuvre']", 'object_name': 'ElementDeProgramme'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'autre': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'caracteristiques': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'elements_de_programme'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['catalogue.CaracteristiqueDElementDeProgramme']"}),
            'classement': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'distribution': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'elements_de_programme'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['catalogue.AttributionDePupitre']"}),
            'documents': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'representations'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['catalogue.Document']"}),
            'etat': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'elements_de_programme'", 'null': 'True', 'to': "orm['catalogue.Etat']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'illustrations': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'representations'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['catalogue.Illustration']"}),
            'oeuvre': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'elements_de_programme'", 'null': 'True', 'to': "orm['catalogue.Oeuvre']"}),
            'personnels': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'elements_de_programme'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['catalogue.Personnel']"})
        },
        'catalogue.engagement': {
            'Meta': {'object_name': 'Engagement'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'devise': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'engagements'", 'null': 'True', 'to': "orm['catalogue.Devise']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'individus': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'engagements'", 'symmetrical': 'False', 'to': "orm['catalogue.Individu']"}),
            'profession': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'engagements'", 'to': "orm['catalogue.Profession']"}),
            'salaire': ('django.db.models.fields.FloatField', [], {'blank': 'True'})
        },
        'catalogue.etat': {
            'Meta': {'ordering': "['slug']", 'object_name': 'Etat'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'nom_pluriel': ('django.db.models.fields.CharField', [], {'max_length': '230', 'blank': 'True'}),
            'publie': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': 'None'})
        },
        'catalogue.evenement': {
            'Meta': {'ordering': "['ancrage_debut']", 'object_name': 'Evenement'},
            'ancrage_debut': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'evenements_debuts'", 'unique': 'True', 'to': "orm['catalogue.AncrageSpatioTemporel']"}),
            'ancrage_fin': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'evenements_fins'", 'unique': 'True', 'null': 'True', 'to': "orm['catalogue.AncrageSpatioTemporel']"}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'circonstance': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'documents': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'evenements'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['catalogue.Document']"}),
            'etat': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'evenements'", 'null': 'True', 'to': "orm['catalogue.Etat']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'illustrations': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'evenements'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['catalogue.Illustration']"}),
            'notes': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'programme': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'evenements'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['catalogue.ElementDeProgramme']"}),
            'relache': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'catalogue.genredoeuvre': {
            'Meta': {'ordering': "['slug']", 'object_name': 'GenreDOeuvre'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'nom_pluriel': ('django.db.models.fields.CharField', [], {'max_length': '430', 'blank': 'True'}),
            'parents': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'enfants'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['catalogue.GenreDOeuvre']"}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': 'None'})
        },
        'catalogue.illustration': {
            'Meta': {'ordering': "['image']", 'object_name': 'Illustration'},
            'auteurs': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'illustrations'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['catalogue.Auteur']"}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'commentaire': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '400'}),
            'legende': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'})
        },
        'catalogue.individu': {
            'Meta': {'ordering': "['nom']", 'object_name': 'Individu'},
            'ancrage_approx': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'individus'", 'unique': 'True', 'null': 'True', 'to': "orm['catalogue.AncrageSpatioTemporel']"}),
            'ancrage_deces': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'individus_decedes'", 'unique': 'True', 'null': 'True', 'to': "orm['catalogue.AncrageSpatioTemporel']"}),
            'ancrage_naissance': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'individus_nes'", 'unique': 'True', 'null': 'True', 'to': "orm['catalogue.AncrageSpatioTemporel']"}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'biographie': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'designation': ('django.db.models.fields.CharField', [], {'default': "'S'", 'max_length': '1'}),
            'documents': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'individus'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['catalogue.Document']"}),
            'etat': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'individus'", 'null': 'True', 'to': "orm['catalogue.Etat']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'illustrations': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'individus'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['catalogue.Illustration']"}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'nom_naissance': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'notes': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'parentes': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'individus_orig'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['catalogue.ParenteDIndividus']"}),
            'particule_nom': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'particule_nom_naissance': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'prenoms': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'individus'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['catalogue.Prenom']"}),
            'professions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'individus'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['catalogue.Profession']"}),
            'pseudonyme': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': 'None'}),
            'titre': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'})
        },
        'catalogue.lieu': {
            'Meta': {'ordering': "['nom']", 'unique_together': "(('nom', 'parent'),)", 'object_name': 'Lieu'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'documents': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'lieux'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['catalogue.Document']"}),
            'etat': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'lieux'", 'null': 'True', 'to': "orm['catalogue.Etat']"}),
            'historique': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'illustrations': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'lieux'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['catalogue.Illustration']"}),
            'nature': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'lieux'", 'to': "orm['catalogue.NatureDeLieu']"}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'notes': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'enfants'", 'null': 'True', 'to': "orm['catalogue.Lieu']"}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': 'None'})
        },
        'catalogue.naturedelieu': {
            'Meta': {'ordering': "['slug']", 'object_name': 'NatureDeLieu'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'nom_pluriel': ('django.db.models.fields.CharField', [], {'max_length': '430', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': 'None'})
        },
        'catalogue.oeuvre': {
            'Meta': {'ordering': "['genre', 'slug']", 'object_name': 'Oeuvre'},
            'ancrage_creation': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'oeuvres_creees'", 'unique': 'True', 'null': 'True', 'to': "orm['catalogue.AncrageSpatioTemporel']"}),
            'auteurs': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'oeuvres'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['catalogue.Auteur']"}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'caracteristiques': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['catalogue.CaracteristiqueDOeuvre']", 'null': 'True', 'blank': 'True'}),
            'coordination': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'description': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'documents': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'oeuvres'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['catalogue.Document']"}),
            'etat': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'oeuvres'", 'null': 'True', 'to': "orm['catalogue.Etat']"}),
            'filles': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'meres'", 'symmetrical': 'False', 'through': "orm['catalogue.ParenteDOeuvres']", 'to': "orm['catalogue.Oeuvre']"}),
            'genre': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'oeuvres'", 'null': 'True', 'to': "orm['catalogue.GenreDOeuvre']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'illustrations': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'oeuvres'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['catalogue.Illustration']"}),
            'lilypond': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'notes': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'prefixe_titre': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'prefixe_titre_secondaire': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'pupitres': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'oeuvres'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['catalogue.Pupitre']"}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': 'None'}),
            'titre': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'titre_secondaire': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        'catalogue.parentedindividus': {
            'Meta': {'ordering': "['type']", 'object_name': 'ParenteDIndividus'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'individus_cibles': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'enfances_cibles'", 'symmetrical': 'False', 'to': "orm['catalogue.Individu']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'parentes'", 'to': "orm['catalogue.TypeDeParenteDIndividus']"})
        },
        'catalogue.parentedoeuvres': {
            'Meta': {'ordering': "['type']", 'unique_together': "(('type', 'mere', 'fille'),)", 'object_name': 'ParenteDOeuvres'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'fille': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'parentes_meres'", 'to': "orm['catalogue.Oeuvre']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mere': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'parentes_filles'", 'to': "orm['catalogue.Oeuvre']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'parentes'", 'to': "orm['catalogue.TypeDeParenteDOeuvres']"})
        },
        'catalogue.partie': {
            'Meta': {'ordering': "['classement', 'nom']", 'object_name': 'Partie'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'classement': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'nom_pluriel': ('django.db.models.fields.CharField', [], {'max_length': '230', 'blank': 'True'}),
            'parente': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'enfant'", 'null': 'True', 'to': "orm['catalogue.Partie']"}),
            'professions': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'parties'", 'symmetrical': 'False', 'to': "orm['catalogue.Profession']"})
        },
        'catalogue.personnel': {
            'Meta': {'object_name': 'Personnel'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'engagements': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'personnels'", 'symmetrical': 'False', 'to': "orm['catalogue.Engagement']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'saison': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'personnels'", 'to': "orm['catalogue.Saison']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'personnels'", 'to': "orm['catalogue.TypeDePersonnel']"})
        },
        'catalogue.prenom': {
            'Meta': {'ordering': "['prenom', 'classement']", 'object_name': 'Prenom'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'classement': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'favori': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prenom': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'catalogue.profession': {
            'Meta': {'ordering': "['slug']", 'object_name': 'Profession'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'nom_feminin': ('django.db.models.fields.CharField', [], {'max_length': '230', 'blank': 'True'}),
            'nom_pluriel': ('django.db.models.fields.CharField', [], {'max_length': '230', 'blank': 'True'}),
            'parente': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'enfant'", 'null': 'True', 'to': "orm['catalogue.Profession']"}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': 'None'})
        },
        'catalogue.pupitre': {
            'Meta': {'ordering': "['partie']", 'object_name': 'Pupitre'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'partie': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pupitres'", 'to': "orm['catalogue.Partie']"}),
            'quantite_max': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'quantite_min': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        'catalogue.saison': {
            'Meta': {'ordering': "['lieu', 'debut']", 'object_name': 'Saison'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'debut': ('django.db.models.fields.DateField', [], {}),
            'fin': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lieu': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'saisons'", 'to': "orm['catalogue.Lieu']"})
        },
        'catalogue.source': {
            'Meta': {'ordering': "['date', 'nom', 'numero', 'page', 'type']", 'object_name': 'Source'},
            'auteurs': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'sources'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['catalogue.Auteur']"}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'contenu': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'documents': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'sources'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['catalogue.Document']"}),
            'etat': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'sources'", 'null': 'True', 'to': "orm['catalogue.Etat']"}),
            'evenements': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'sources'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['catalogue.Evenement']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'illustrations': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'sources'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['catalogue.Illustration']"}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'notes': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'page': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sources'", 'to': "orm['catalogue.TypeDeSource']"})
        },
        'catalogue.typedecaracteristiquedoeuvre': {
            'Meta': {'ordering': "['classement']", 'object_name': 'TypeDeCaracteristiqueDOeuvre'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'classement': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'nom_pluriel': ('django.db.models.fields.CharField', [], {'max_length': '230', 'blank': 'True'})
        },
        'catalogue.typedeparentedindividus': {
            'Meta': {'ordering': "['classement']", 'object_name': 'TypeDeParenteDIndividus'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'classement': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'nom_pluriel': ('django.db.models.fields.CharField', [], {'max_length': '55', 'blank': 'True'})
        },
        'catalogue.typedeparentedoeuvres': {
            'Meta': {'ordering': "['classement']", 'object_name': 'TypeDeParenteDOeuvres'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'classement': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'nom_relatif': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'nom_relatif_pluriel': ('django.db.models.fields.CharField', [], {'max_length': '130', 'blank': 'True'})
        },
        'catalogue.typedepersonnel': {
            'Meta': {'ordering': "['nom']", 'object_name': 'TypeDePersonnel'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'catalogue.typedesource': {
            'Meta': {'ordering': "['slug']", 'object_name': 'TypeDeSource'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'nom_pluriel': ('django.db.models.fields.CharField', [], {'max_length': '230', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': 'None'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['catalogue']