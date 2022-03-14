
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
from distributions import Distributions
pio.templates.default = 'plotly_dark'
np.seterr(divide='ignore')


class Plots(Distributions):

    def __init__(self, fit, df):

        log_returns = self.get_log_return(df)
        dist_function = self.dist_dict()[fit]
        distribution = dist_function(log_returns)
        self.bic = distribution[1]
        self.aic = distribution[2]
        xs = distribution[3]
        pdf = distribution[4]
        self.mu = distribution[6]
        self.beta = distribution[7]
        self.fig = self.dist_plot(log_returns, xs, pdf)
        
    def get_plot_list(self):
        return self.PLOT_LIST

    def dist_plot(self, returns, xs, pdf):

        fig1 = px.histogram(returns, histnorm='probability density')
        fig1.add_trace(go.Scatter(x=xs, y=pdf, name='Function'))
        fig1.update_layout(xaxis_title='Distribution',
                           legend_title='',
                           legend=dict(
                               orientation="h",
                               yanchor="bottom",
                               y=1.02,
                               xanchor="center",
                               x=0.5
                           ))

        return fig1

    #### dictionary: fit name : fit function from super ####
    def dist_dict(self):

        plot_dict = {

            'Normal Fit': super().normal_fit,
            'Pnormal Fit': super().pnorm_fit,
            'Log Normal Fit': super().lognormal_fit,
            'PLog Normal Fit': super().plognorm_fit,
            'Exponential Fit': super().expon_fit,
            'Laplace Fit': super().laplace_fit,
            'Asymmetric Laplace Fit': super().laplace_fit,
            'Cauchy Fit': super().cauchy_fit,
            'Skew Cauchy Fit': super().cauchy_fit,
            'Chi Fit': super().chi_fit,
            'Chi Squared Fit': super().chi2_fit,
            'T Distribution Fit': super().tdist_fit,
            'Gamma Fit': super().gamma_fit,
            'Weibull Exponential Fit': super().weibullexpon_fit,
            'Weibull Minimum Fit': super().weibullmin_fit,
            'Weibull Maximum Fit': super().weibullmax_fit,
            'Johnsonsu Fit': super().johnsonsu_fit,
            'Generalized Hyperbolic Fit': super().genhyperbolic_fit,
            'Generalized Extreme Value Fit': super().genextreme_fit,
            'Tukey Lambda Fit': super().turklamda_fit
        }

        return plot_dict

    def get_log_return(self, df):
        df["logReturn"] = np.log(df.Close/df.Close.shift(1)).dropna()
        return df.logReturn[1:]

    @classmethod
    def top_3_fits(cls, df):

        aic_scores = {}
        bic_scores = {}
        log_return = cls.get_log_return(cls, df)
        distributions = cls.dist_dict(cls)

        for key, fit in distributions.items():

            params = fit(Distributions(), log_return)
            bic = params[1]
            aic = params[2]
            bic_scores[key] = bic
            aic_scores[key] = aic
            bic_sorted_scores = sorted(
                bic_scores.items(), key=lambda x: x[1], reverse=False)
            aic_sorted_scores = sorted(
                aic_scores.items(), key=lambda x: x[1], reverse=False)

        return bic_sorted_scores[:3], aic_sorted_scores[:3]

    @classmethod
    def get_plot_list(cls):

        return list(cls.dist_dict(cls).keys())
