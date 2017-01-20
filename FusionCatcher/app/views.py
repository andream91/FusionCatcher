from app.models import Gene,Chromosome,CellLine
import json

# Create your views here.
from django.http import HttpResponse

def search_for_chromosome(request,c_line,chromos,start_point,end_point):
    response = []
    header = ["Cell line",
        "Gene pair symbols",
        "Gene pair EnsIDs",
        "Exon pair",
        "Chromosome : fusion point : strand",
        "Description",
        "Counts of common mapping reads",
        "Spanning pairs",
        "Spanning unique reads",
        "Longest anchor found",
        "Fusion finding method",
        "Fusion sequence",
        "Predicted effect",
        "Predicted fused transcripts",
        "Predicted fused proteins"]
    
    for fusions in CellLine.nodes.get(cell_line = c_line).happen:
        for chromosome in fusions.at_chromosome:
            for chrom in chromosome.nodes.filter(id__exact=chromos):
                for chro in chrom.fromFusionToChromosome.filter(fusion_point__gt=start_point):
                    for res in chro.fromFusionToChromosome.filter(fusion_point__lt=end_point):
                        print([{"value": res.id}, {"value": res.fusion_point}])
            
    
    return HttpResponse(json.dumps(response))