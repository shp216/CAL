import ml_collections
import torch
from path import Path


def get_config():
    """Gets the default hyperparameter configuration."""

    config = ml_collections.ConfigDict()
    config.log_dir = Path("logs") 
    # Exp info
    config.dataset_path = Path("dataset") 
    config.train_json = config.dataset_path / 'train.json'
    config.val_json = config.dataset_path / 'val.json'

    config.resume_from_checkpoint = None

    config.dataset = "publaynet"
    config.max_num_comp = 9

    # Training info
    config.seed = 42
    # data specific
    config.categories_num = 7
    # model specific
    config.latent_dim = 512
    config.num_layers = 4
    config.num_heads = 8
    config.dropout_r = 0.0
    config.activation = "gelu"
    config.cond_emb_size = 224
    config.cls_emb_size = 64
    # diffusion specific
    config.num_cont_timesteps = 100
    config.num_discrete_steps = 10
    config.beta_schedule = "squaredcos_cap_v2"

    # Training info
    config.log_interval = 2647
    config.save_interval = 50_000

    # # 옵티마이저 설정을 위한 ConfigDict 인스턴스 생성
    # optimizer = ml_collections.ConfigDict()

    # # 설정 추가
    # optimizer.learning_rate = 0.001
    # optimizer.type = "Adam"
    # optimizer.beta1 = 0.9
    # optimizer.beta2 = 0.999
    config.optimizer = ml_collections.ConfigDict()
    config.optimizer.num_gpus = torch.cuda.device_count()

    config.optimizer.mixed_precision = 'no'
    config.optimizer.gradient_accumulation_steps = 1
    config.optimizer.betas = (0.95, 0.999)
    config.optimizer.epsilon = 1e-8
    config.optimizer.weight_decay = 1e-6

    config.optimizer.lr_scheduler = 'cosine'
    config.optimizer.num_warmup_steps = 100_000
    config.optimizer.lr = 0.0001

    config.optimizer.num_epochs = 800
    config.optimizer.batch_size = 64
    config.optimizer.split_batches = False
    config.optimizer.num_workers = 4

    config.optimizer.lmb = 5

    if config.optimizer.num_gpus == 0:
        config.device = 'cpu'
    else:
        config.device = 'cuda'
    return config