class BuildValidator:
    def __init__(self, custom_pc_build):
        self.custom_pc_build = custom_pc_build
        self.validation_errors = []

    def validate(self):
        self.validate_cpu()
        self.validate_memory()
        self.validate_storage()
        self.validate_gpu()
        self.validate_psu()
        self.validate_case()
        return self.validation_errors

    def validate_cpu(self):
        cpu = self.custom_pc_build.get('cpu')
        if not cpu:
            self.validation_errors.append(VALIDATION_ERROR_MSG.format('CPU is missing'))
        # Additional CPU validation logic goes here

    def validate_memory(self):
        memory = self.custom_pc_build.get('memory')
        if not memory:
            self.validation_errors.append(VALIDATION_ERROR_MSG.format('Memory is missing'))
        # Additional memory validation logic goes here

    def validate_storage(self):
        storage = self.custom_pc_build.get('storage')
        if not storage:
            self.validation_errors.append(VALIDATION_ERROR_MSG.format('Storage is missing'))
        # Additional storage validation logic goes here

    def validate_gpu(self):
        gpu = self.custom_pc_build.get('gpu')
        if not gpu:
            self.validation_errors.append(VALIDATION_ERROR_MSG.format('GPU is missing'))
        # Additional GPU validation logic goes here

    def validate_psu(self):
        psu = self.custom_pc_build.get('psu')
        if not psu:
            self.validation_errors.append(VALIDATION_ERROR_MSG.format('PSU is missing'))
        # Additional PSU validation logic goes here

    def validate_case(self):
        case = self.custom_pc_build.get('case')
        if not case:
            self.validation_errors.append(VALIDATION_ERROR_MSG.format('Case is missing'))
        # Additional case validation logic goes here

# Example usage:
# validator = BuildValidator(custom_pc_build)
# errors = validator.validate()
# if errors:
#     # Handle validation errors
# else:
#     # Proceed with build
