from .schnet import SchNetEncoder
from .cftfm import CFTransformerEncoder, HierEncoder
from .gnn import GNN_graphpred, MLP, WeightGNN


def get_encoder(config, device):
    if config.name == 'schnet':
        return SchNetEncoder(
            hidden_channels = config.hidden_channels,
            num_filters = config.num_filters,
            num_interactions = config.num_interactions,
            edge_channels = config.edge_channels,
            cutoff = config.cutoff,
        )
    elif config.name == 'cftfm':
        return CFTransformerEncoder(
            hidden_channels = config.hidden_channels,
            edge_channels = config.edge_channels,
            key_channels = config.key_channels,
            num_heads = config.num_heads,
            num_interactions = config.num_interactions,
            k = config.knn,
            cutoff = config.cutoff,
        )
    elif config.name == 'hierGT':
        return HierEncoder(
            hidden_channels = config.hidden_channels,
            edge_channels = config.edge_channels,
            key_channels = config.key_channels,
            num_heads = config.num_heads,
            num_interactions = config.num_interactions,
            k = config.knn,
            cutoff = config.cutoff,
            device = device
        )
    else:
        raise NotImplementedError('Unknown encoder: %s' % config.name)
