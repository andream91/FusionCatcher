from neomodel import (StructuredNode, StructuredRel, StringProperty, IntegerProperty, ArrayProperty)
from neomodel.relationship_manager import RelationshipTo, RelationshipFrom

#EDGES
class AT_CHROMOSOME(StructuredRel):
    fusion_point = IntegerProperty()

class AT_EXON(StructuredRel):
    fusion_partner = StringProperty()

class HAD_FUSION(StructuredRel):
    predicted_effect = StringProperty()
    strand = StringProperty()
    
class IN_COUPLE(StructuredRel):
    position = IntegerProperty()
    
class WITH_GENE(StructuredRel):
    predicted_effect = StringProperty()
    strand = StringProperty()
    
class WITH_OTHER_TRANSCRIPT(StructuredRel):
    position = IntegerProperty()   
    
class WITH_VIRUSES(StructuredRel):
    count_of_mapping_reads = IntegerProperty()
#NODES

class CellLine(StructuredNode):
    cell_line = StringProperty()
    #
    happen = RelationshipTo('Fusion',"HAPPEN")
    with_viruses = RelationshipTo('Virus',"WITH_VIRUSES",model=WITH_VIRUSES)
    
class Couple(StructuredNode):
    id = IntegerProperty() 
    #
    with_other_transcript = RelationshipTo('Transcript',"WITH_OTHER_TRANSCRIPT", model=WITH_OTHER_TRANSCRIPT)
    with_protein = RelationshipTo('Protein',"WITH_PROTEIN")
    #
    fromTranscriptToCouple = RelationshipFrom('Transcript',"IN_COUPLE")
    fromFusionToCouple = RelationshipFrom('Fusion',"WITH_TRANS_COUPLE")
    
class Chromosome(StructuredNode):
    id = StringProperty()
    #
    of_gene = RelationshipTo('Gene',"OF_GENE")
    #
    fromFusiontoChromosome = RelationshipFrom('Fusion', "AT_CHROMOSOME", model=AT_CHROMOSOME)
    
class Exon(StructuredNode):
    id = StringProperty()
    #
    in_gene = RelationshipTo('Gene',"IN_GENE")
    #
    fromFusionToExon = RelationshipFrom('Fusion', "AT_EXON", model=AT_EXON)
    
class Fusion(StructuredNode):
    id = IntegerProperty()
    description = ArrayProperty()
    common_mapping_reads = IntegerProperty()
    spanning_pairs = IntegerProperty()
    spanning_unique_reads = IntegerProperty()
    longest_anchor_found = IntegerProperty()
    fusion_finding_method = StringProperty()
    fusion_sequence = StringProperty()
    #
    at_chromosome = RelationshipTo('Chromosome', "AT_CHROMOSOME", model=AT_CHROMOSOME)
    at_exon = RelationshipTo('Exon', "AT_EXON", model=AT_EXON)
    with_trans_couple = RelationshipTo('Couple', "WITH_TRANS_COUPLE")
    with_gene = RelationshipTo('Gene',"WITH_GENE", model=WITH_GENE)
    #
    fromCellLineToFusion = RelationshipFrom('CellLine',"HAPPEN")
    fromGeneToFusion = RelationshipFrom('Fusion', "HAD_FUSION", model=HAD_FUSION)

class Gene(StructuredNode):
    id = StringProperty()
    symbol = StringProperty()
    #
    had_fusion = RelationshipTo('Fusion', "HAD_FUSION", model=HAD_FUSION)
    #
    fromFusionToGene = RelationshipFrom('Fusion',"WITH_GENE", model=WITH_GENE)
    fromExonToGene = RelationshipFrom('Exon',"IN_GENE")
    fromChromosomeToGene = RelationshipFrom('Chromosome',"OF_GENE")
    
class Protein(StructuredNode):
    id = StringProperty()
    #
    fromCoupleToProtein = RelationshipFrom('Couple',"WITH_PROTEIN")
    
class Transcript(StructuredNode):
    id = StringProperty()
    #
    in_couple = RelationshipTo('Couple',"IN_COUPLE", model=IN_COUPLE)
    #
    fromCoupleToTranscript = RelationshipFrom('Couple',"WITH_OTHER_TRANSCRIPT", model=WITH_OTHER_TRANSCRIPT)

    
class Virus(StructuredNode):
    name = StringProperty()
    gi = StringProperty()
    ref = StringProperty()
    #
    fromCellLineToVirus = RelationshipFrom('CellLine',"WITH_VIRUSES", model=WITH_VIRUSES)