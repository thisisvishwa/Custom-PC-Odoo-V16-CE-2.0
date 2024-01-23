class CompatibilityChecker:
    def __init__(self, components):
        self.components = components

    def check_power_compatibility(self):
        # Placeholder for power compatibility logic
        # This should check if the power supply can handle the total power consumption of all components
        pass

    def check_size_compatibility(self):
        # Placeholder for size compatibility logic
        # This should check if the components will physically fit inside the chosen case
        pass

    def check_connectivity_compatibility(self):
        # Placeholder for connectivity compatibility logic
        # This should check if all components have the necessary ports and connectors to interface with each other
        pass

    def run_all_checks(self):
        power_compatible = self.check_power_compatibility()
        size_compatible = self.check_size_compatibility()
        connectivity_compatible = self.check_connectivity_compatibility()

        compatibility_results = {
            'power': power_compatible,
            'size': size_compatible,
            'connectivity': connectivity_compatible
        }

        return compatibility_results

    def generate_compatibility_report(self):
        results = self.run_all_checks()
        report = []

        for key, value in results.items():
            if not value:
                report.append(INCOMPATIBLE_COMPONENT_MSG.format(component=key))

        return report if report else ['All components are compatible.']

# Example usage:
# components = {'cpu': ..., 'gpu': ..., 'psu': ..., 'case': ...}
# checker = CompatibilityChecker(components)
# compatibility_report = checker.generate_compatibility_report()