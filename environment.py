import logging


def before_all(context):
    context.logger = logging
    log_filename = './etl_test.log'
    context.logger.basicConfig(format='%(levelname)s: %(asctime)s: %(message)s', filename=log_filename, level=logging.INFO)
    context.logger.info('Beginning of test')


def after_all(context):
    context.logger.info('End of test')


def before_scenario(context, scenario):
    context.logger.info("Beginning of scenario: " + scenario.name)


def after_scenario(context, scenario):
    context.logger.info("End of scenario: " + scenario.name)


def before_feature(context, feature):
    context.logger.info("Beginning of feature: " + feature.name)


def after_feature(context, feature):
    context.logger.info("End of feature: " + feature.name)


def before_step(context, step):
    context.logger.info("Beginning of step: " + step.name)


def after_step(context, step):
    context.logger.info("End of step: " + step.name)
